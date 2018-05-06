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


# blood pressure path
stateMap = {
    'welcome-greeting': {
        'text-template': 'bp-greeting',
        'yes': {
            'next-state': 'bp-measurement-yes',
        }
    },
    'bp-measurement-yes': {
        'text-template': 'bp-measurement-yes',
        'next-state': 'bp-measurement-confirm'
    },
    'bp-measurement-confirm': {
        'text-template': 'bp-measurement-confirm',
        'yes': {
            'next-state': 'aspirin',
        }
    },
    'aspirin': {
        'text-template': 'bp-aspirin-prompt',
        'no': {
            'next-state': 'send-to-dr',
        }
    },
    'send-to-dr': {
        'text-template': 'bp-send-to-dr',
        'yes': {
            'next-state': 'good-bye',
        }
    },
    'good-bye': {
        'text-template': 'bp-thank-you'
    }
}


class State:
    def __init__(self):
        self.current = "welcome-greeting"

    def start(self):
        self.current = "welcome-greeting"

    def nextYes(self):
        self.current = stateMap[self.current]['yes']['next-state']

    def nextNo(self):
        self.current = stateMap[self.current]['no']['next-state']

    def next(self):
        self.current = stateMap[self.current]['next-state']

    def text_template(self):
        return stateMap[self.current]['text-template']


app = Flask(__name__)
ask = Ask(app, '/ask/')
CORS(app)

# Initialize the sponsor APIs
redox_api = RedoxAPI()
wallet = SoftheonWalletAPI(
    os.environ.get('SOFTHEON_CLIENT_ID', ''),
    os.environ.get('SOFTHEON_CLIENT_SECRET', '')
)


state = State()

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


@ask.intent('YesIntent')
def yes_intent():
    state.nextYes()
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
    state.next()
    pill_amount = redox_api.medication_count()

    if amount != pill_amount:
        text = render_template('incorrect-pill-count', amount=pill_amount)
        return statement(text)

    text = render_template('correct-pill-count')
    return statement(text)


@ask.intent('MedicationListIntent')
def medication_list_intent():
    medication_list = ', '.join(redox_api.medications())
    count = len(medication_list)
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
