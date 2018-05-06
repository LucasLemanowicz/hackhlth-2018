import os

from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from flask_ask import (
    Ask,
    question,
    request as ask_request,
    session as ask_session,
    statement
)
from redox import RedoxAPI
from softheon import SoftheonWalletAPI
from statemaps import BP_STATEMAP, PR_STATEMAP, FINAL_STATEMAP
from utils import clean_medication_name, human_and, human_or


class State:
    def __init__(self, stateMap):
        self.current = 'welcome-greeting'
        self.stateMap = stateMap

    def updateState(self, stateMap):
        self.stateMap = stateMap

    def start(self):
        self.current = 'welcome-greeting'

    def nextYes(self):
        self.current = self.stateMap[self.current]['yes']['next-state']

    def nextNo(self):
        self.current = self.stateMap[self.current]['no']['next-state']

    def next(self):
        self.current = self.stateMap[self.current]['next-state']

    def text_template(self):
        return self.stateMap[self.current]['text-template']

app = Flask(__name__)
ask = Ask(app, '/ask/')
CORS(app)

# Initialize the sponsor APIs
redox_api = RedoxAPI(
    os.environ.get('REDOX_API_KEY', ''),
    os.environ.get('REDOX_SOURCE_SECRET', '')
)
wallet = SoftheonWalletAPI(
    os.environ.get('SOFTHEON_CLIENT_ID', ''),
    os.environ.get('SOFTHEON_CLIENT_SECRET', '')
)

state = State(BP_STATEMAP)

# Web Endpoints
@app.route('/', methods=['GET'])
def home():
    return render_template('hello-world')


@app.route('/setWorkflow/<path>', methods=['GET'])
def set_workflow(path):
    if path == 'blood':
        state.updateState(BP_STATEMAP)
        return 'Updated to Blood Pressure Workflow'

    if path == 'refill':
        state.updateState(PR_STATEMAP)
        return 'Updated to Refill Prescription Workflow'

    if path == 'final':
        state.updateState(FINAL_STATEMAP)
        return 'Updated to FINAL Workflow'


# Redox Ednpoints
@app.route('/redox', methods=['GET', 'POST'])
def redox():
    verification_token = request.headers.get('verification-token', '')
    if verification_token != os.environ.get('REDOX_VERIFICATION_TOKEN', ''):
        return render_template('redox-verification-error')

    if 'challenge' in request.args:
        return request.args.get('challenge')

    redox_api.transmission = request.get_json()
    return ''


@app.route('/redox/data', methods=['GET'])
def redox_data():
    return jsonify(redox_api.transmission)


# Amazon Alexa Endpoints
@ask.launch
def launched():
    state.start()
    text = render_template(state.text_template())
    return question(text)


@ask.intent('PRPathIntent')
def set_state_map_pr():
    state.updateState(PR_STATEMAP)
    return statement('Okay, path changed to refill')


@ask.intent('YesIntent')
def yes_intent():
    state.nextYes()
    if state.current == 'pr-refill':
        return payment(28, 'mastercard')
    if state.current == 'bp-thanks-and-good-bye':
        text = render_template(state.text_template())
        return question(text).standard_card(
            title='Blood Pressure Chart',
            text='Blood pressure has been steadily rising',
            small_image_url='https://i.imgur.com/S0Por4w.png',
            large_image_url='https://i.imgur.com/S0Por4w.png')

    text = render_template(state.text_template())
    return question(text)


@ask.intent('NoIntent')
def no_intent():
    state.nextNo()
    if state.current == 'pr-card-check-no':
        return payment(28)
    text = render_template(state.text_template())
    return question(text)


@ask.intent('BPIntent', convert={'systolic': int, 'diastolic': int})
def bp_intent(systolic, diastolic):
    state.next()
    text = render_template('bp-measurement-confirm',
                           systolic=systolic,
                           diastolic=diastolic)
    return question(text)


@ask.intent('PillCountIntent', convert={'amount': int})
def pill_count_intent(amount):
    pill_amount = redox_api.medication_count()
    medications = [clean_medication_name(m) for m in redox_api.medications()]
    medication_list = human_and(medications)

    if amount != pill_amount:
        text = render_template('pr-incorrect-pill-count', amount=pill_amount)
        return question(text)

    state.next()
    text = render_template('pr-pill-count-confirmation',
                           medications=medication_list,
                           low_on=medications[0])
    return question(text)

@ask.intent('CardIntent')
def use_different_card(cardname):
    return payment(28, cardname)


@ask.intent('MedicationListIntent')
def medication_list_intent():
    medications = [clean_medication_name(m) for m in redox_api.medications()]
    medication_list = human_and(medications)
    count = len(medications)

    text = render_template('medication-list',
                           medications=medication_list,
                           count=count)
    return question(text)


# Appointment Scheduling
@ask.intent('ScheduleVisitAvailabilityIntent')
def schedule_visit_availability_intent():
    availability = [str(x) for x in redox_api.get_schedule()]
    availability_ord = human_or(availability)

    text = render_template('schedule-availability', times=availability_ord)
    return question(text)


@ask.intent('MakeAppointmentIntent', convert={'hour': int})
def make_appointment_intent(hour):
    availability = redox_api.get_schedule()
    availability_ord = human_or([str(x) for x in availability])
    if hour not in availability:
        text = render_template('schedule-conflict',
                               hour=hour,
                               times=availability_ord)
        return question(text)

    redox_api.make_appointment(hour)

    text = render_template('make-appointment', hour=hour)
    card = render_template('make-appointment-card', hour=hour)

    return question(text).simple_card(card)


@ask.session_ended
def session_ended():
    return '{}', 200


@ask.intent('HelloIntent')
def hello(firstname):
    text = render_template('hello-name', name=firstname)
    return statement(text).simple_card('Hello', text)


@ask.intent('PaymentIntent')
def payment(amount, card):

    payment_failure = render_template('payment-failure')
    payment_success = render_template('payment-success', amount=amount, card=card)

    status, data = wallet.make_payment(amount)
    if not status:
        return question(payment_failure)

    transaction_id = data.get('result', []).get('merchantTransactionId', '-1')
    success_card = render_template('payment-success-card',
                                   amount=amount,
                                   transaction_id=transaction_id)

    return question(payment_success).simple_card(success_card)


# Launch the server
if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=int(os.environ.get('PORT', 2020)))
