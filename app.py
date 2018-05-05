import os

from flask import Flask
from flask_cors import CORS
from flask_ask import Ask, statement


app = Flask(__name__)
ask = Ask(app, '/ask/')
CORS(app)


@app.route('/', methods=['GET'])
def home():
    return 'Hello, world!'

@ask.intent('HelloIntent')
def hello(firstname):
    text = 'Hello, ' + firstname
    return statement(text).simple_card('Hello', text)


if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=int(os.environ.get('PORT', 2020)))

