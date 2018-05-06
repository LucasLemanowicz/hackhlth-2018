import os

from flask import Flask
from flask_cors import CORS
from flask_ask import Ask, statement
from softheon import SoftheonWalletAPI


app = Flask(__name__)
ask = Ask(app, '/ask/')
CORS(app)

# Initialize the Softheon Wallet for payment processing
wallet = SoftheonWalletAPI(
    os.environ.get('SOFTHEON_CLIENT_ID', ''),
    os.environ.get('SOFTHEON_CLIENT_SECRET', '')
)


@app.route('/', methods=['GET'])
def home():
    return 'Hello, world!'


@ask.intent('HelloIntent')
def hello(firstname):
    text = 'Hello, ' + firstname
    return statement(text).simple_card('Hello', text)


@ask.intent('PaymentIntent')
def payment(amount):

    PAYMENT_FAILURE = 'Payment failed, please try again.'
    PAYMENT_SUCCESS = 'Payment of {} dollars succeeded. Thank you.'.format(
        amount)

    status, data = wallet.make_payment(amount)
    if not status:
        return statement(PAYMENT_FAILURE)

    success_card = 'Payment of ${} succeeded (Transaction ID: {})'.format(
        data.get('paymentAmount', '0.00'),
        data.get('result', []).get('merchantTransactionId', '422806694271965000')
    )
    return statement(PAYMENT_SUCCESS).simple_card(success_card)


if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=int(os.environ.get('PORT', 2020)))
