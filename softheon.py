import base64
import json
import os

import requests

from scaffolding import CREDIT_CARD


class SoftheonWalletAPI:
    TOKEN_ENDPOINT = 'https://hack.softheon.io/oauth2/connect/token'
    CREDITCARD_ENDPOINT = 'https://hack.softheon.io/api/payments/v1/creditcards'
    PAYMENT_ENDPOINT = 'https://hack.softheon.io/api/payments/v1/payments'

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = self._get_access_token(client_id, client_secret)

    def _get_access_token(self, client_id, client_secret):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = {
            'scope': 'paymentapi',
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret
        }

        http = requests.post(self.TOKEN_ENDPOINT, headers=headers, data=body)
        resp = json.loads(http.text)

        return resp['access_token']

    def _get_credit_card_token(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.access_token
        }

        body = str(CREDIT_CARD)

        http = requests.post(self.CREDITCARD_ENDPOINT, headers=headers,
                             data=body)
        resp = json.loads(http.text)

        return resp['token']

    def make_payment(self, payment_amount):
        """ Make a payment to your provider """
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.access_token
        }

        body = str({
            'paymentAmount': payment_amount,
            'paymentMethod': {
                'paymentToken': str(self._get_credit_card_token()),
                'type': 'Credit Card'
            }
        })

        http = requests.post(self.PAYMENT_ENDPOINT, headers=headers, data=body)
        resp = json.loads(http.text)

        return (resp.get('result', []).get('message', '') == 'Success', resp)
