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

        # Unfortunately the API call above is not implemented, so we return an
        # object with available time slots for that given day
        return [2, 3, 5]

    def make_appointment(self, hour):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.access_token
        }
        body = {
            'Meta': {
                'DataModel': 'Scheduling',
                'EventType': 'New'
            },
            'Visit': {
                'VisitNumber': '1234',
                'VisitDateTime': '2018-05-03T{}:00:00.000Z'.format(12 + hour),
                'Duration': 60,
                'Location': {
                    'Department': 'Medication Department'
                }
            }
        }

        http = requests.post(self.REDOX_ENDPOINT, headers=headers, json=body)
        resp = http.content

        print(resp)
        return True

    def medication_count(self):
        return len(self.transmission.get('Medications', []))

    def medications(self):
        if 'Medications' not in self.transmission:
            return []

        return [m['Product']['Name'] for m in self.transmission['Medications']]
