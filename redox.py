import json

import requests

from scaffolding import CLINICAL_SUMMARY


class RedoxAPI:
    TOKEN_ENDPOINT = 'https://api.redoxengine.com/auth/authenticate'
    REDOX_ENDPOINT = 'https://api.redoxengine.com/endpoint'

    transmission = CLINICAL_SUMMARY

    def __init__(self, api_key, source_secret):
        self.api_key = api_key
        self.source_secret = source_secret
        self.access_token = self._get_access_token(api_key, source_secret)

    def _get_access_token(self, api_key, source_secret):
        headers = {
            'Content-Type': 'application/json'
        }
        body = {
            'apiKey': api_key,
            'secret': source_secret
        }

        http = requests.post(self.TOKEN_ENDPOINT, headers=headers, json=body)
        resp = http.json()

        return resp['accessToken']

    def get_schedule(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.access_token
        }
        body = {
            'Meta': {
                'DataModel': 'Scheduling',
                'EventType': 'AvailableSlots'
            },
            'StartDateTime': '2018-05-03T22:43:16.935Z'
        }

        http = requests.post(self.REDOX_ENDPOINT, headers=headers, json=body)
        resp = http.content

        # TODO: Finish this function
        print(resp)


    def medication_count(self):
        return len(self.transmission.get('Medications', []))

    def medications(self):
        if 'Medications' not in self.transmission:
            return []

        return [m['Product']['Name'] for m in self.transmission['Medications']]
