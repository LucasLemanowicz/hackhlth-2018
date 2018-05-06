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
from statemaps import BP_STATEMAP, PR_STATEMAP
from utils import clean_medication_name, human_and


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
        payment(98)
        return
    text = render_template(state.text_template())
    return question(text)


@ask.intent('NoIntent')
def no_intent():
    state.nextNo()
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

    if amount != pill_amount:
        text = render_template('pr-incorrect-pill-count', amount=pill_amount)
        return statement(text)

    state.next()    
    text = render_template('pr-pill-count-confirmation', amount=pill_amount)
    return question(text)


@ask.intent('MedicationListIntent')
def medication_list_intent():
    medications = [clean_medication_name(m) for m in redox_api.medications()]
    medication_list = human_and(medications)
    count = len(medications)

    text = render_template('medication-list',
                           medications=medication_list,
                           count=count)
    return statement(text)


@ask.session_ended
def session_ended():
    return '{}', 200


@ask.intent('HelloIntent')
def hello(firstname):
    text = render_template('hello-name', name=firstname)
    return statement(text).simple_card('Hello', text)


@ask.intent('PaymentIntent')
def payment(amount):

    payment_failure = render_template('payment-failure')
    payment_success = render_template('payment-success', amount=amount)

    status, data = wallet.make_payment(amount)
    if not status:
        return statement(payment_failure)

    transaction_id = data.get('result', []).get('merchantTransactionId', '-1')
    success_card = render_template('payment-success-card',
                                   amount=amount,
                                   transaction_id=transaction_id)

    return statement(payment_success).simple_card(success_card)


# Launch the server
if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=int(os.environ.get('PORT', 2020)))
