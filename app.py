import os

from flask import Flask, render_template
from flask_cors import CORS
from flask_ask import (
    Ask,
    request as ask_request,
    session as ask_session,
    statement
)
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
    return render_template('hello-world')


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


if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=int(os.environ.get('PORT', 2020)))
