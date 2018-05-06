from scaffolding import CLINICAL_SUMMARY


class RedoxAPI:
    transmission = CLINICAL_SUMMARY

    def __init__(self, transmission=None):
        if transmission is not None:
            self.transmission = transmission

    def medication_count(self):
        return len(self.transmission.get('Medications', []))

    def medications(self):
        if 'Medications' not in self.transmission:
            return []

        return [m['Product']['Name'] for m in self.transmission['Medications']]


if __name__ == '__main__':
    redox_api = RedoxAPI()
    print(redox_api.medication_count())
    print(redox_api.medications())
