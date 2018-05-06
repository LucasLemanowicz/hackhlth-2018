BILLING_ADDRESS = {
    'address1': '111 test',
    'address2': '111 test',
    'city': 'Stony Brook',
    'state': 'NY',
    'zipCode': '11111'
}

CREDIT_CARD = {
    'cardNumber': '4134185779995000',
    'securityCode': '123',
    'expirationMonth': 3,
    'expirationYear': 2018,
    'cardHolderName': 'Test',
    'billingAddress': BILLING_ADDRESS,
    'email': 'example@example.com',
}

CLINICAL_SUMMARY = {
    'AdvanceDirectives': [
        {
            'Code': '304253006',
            'CodeSystem': '2.16.840.1.113883.6.96',
            'CodeSystemName': 'SNOMED CT',
            'Custodians': [
                {
                    'Address': {
                        'City': 'Burlington',
                        'Country': 'USA',
                        'State': 'MA',
                        'StreetAddress': '21 North Ave.',
                        'ZIP': '02368'
                    },
                    'Credentials': 'Dr.',
                    'FirstName': 'Robert',
                    'LastName': 'Dolin'
                }
            ],
            'EndDate': None,
            'ExternalReference': 'AdvanceDirective.b50b7910-7ffb-4f4c-bbe4-177ed68cbbf3.pdf',
            'Name': 'Do not resuscitate',
            'StartDate': '2011-02-13T05:00:00.000Z',
            'Type': {
                'Code': '304251008',
                'CodeSystem': '2.16.840.1.113883.6.96',
                'CodeSystemName': 'SNOMED CT',
                'Name': 'Resuscitation'
            },
            'VerifiedBy': [
                {
                    'Credentials': 'Dr.',
                    'DateTime': None,
                    'FirstName': 'Robert',
                    'LastName': 'Dolin'
                }
            ]
        }
    ],
    'Allergies': [
        {
            'Comment': 'Noted when patient took penicillin for ear infection.',
            'Criticality': {
                'Code': 'CRITH',
                'CodeSystem': '2.16.840.1.113883.5.1063',
                'CodeSystemName': 'ObservationValue',
                'Name': 'High criticality'
            },
            'EndDate': None,
            'Reaction': [
                {
                    'Code': '28926001',
                    'CodeSystem': '2.16.840.1.113883.6.96',
                    'CodeSystemName': 'SNOMED CT',
                    'Name': 'Rash',
                    'Severity': {
                        'Code': '255604002',
                        'CodeSystem': '2.16.840.1.113883.6.96',
                        'CodeSystemName': 'SNOMED CT',
                        'Name': 'Mild'
                    },
                    'Text': None
                },
                {
                    'Code': '247472004',
                    'CodeSystem': '2.16.840.1.113883.6.96',
                    'CodeSystemName': 'SNOMED CT',
                    'Name': 'Hives',
                    'Severity': {
                        'Code': '6736007',
                        'CodeSystem': '2.16.840.1.113883.6.96',
                        'CodeSystemName': 'SNOMED CT',
                        'Name': 'Moderate'
                    },
                    'Text': None
                }
            ],
            'Severity': {
                'Code': '6736007',
                'CodeSystem': '2.16.840.1.113883.6.96',
                'CodeSystemName': 'SNOMED CT',
                'Name': 'Moderate'
            },
            'StartDate': None,
            'Status': {
                'Code': '73425007',
                'CodeSystem': '2.16.840.1.113883.6.96',
                'CodeSystemName': 'SNOMED CT',
                'Name': 'Inactive'
            },
            'Substance': {
                'Code': '7982',
                'CodeSystem': '2.16.840.1.113883.6.88',
                'CodeSystemName': 'RxNorm',
                'Name': 'Penicillin G benzathine'
            },
            'Type': {
                'Code': '419511003',
                'CodeSystem': '2.16.840.1.113883.6.96',
                'CodeSystemName': 'SNOMED CT',
                'Name': 'Propensity to adverse reaction to drug'
            }
        },
        {
            'Comment': None,
            'Criticality': {
                'Code': 'CRITL',
                'CodeSystem': '2.16.840.1.113883.5.1063',
                'CodeSystemName': 'ObservationValue',
                'Name': 'Low criticality'
            },
            'EndDate': None,
            'Reaction': [
                {
                    'Code': '267036007',
                    'CodeSystem': '2.16.840.1.113883.6.96',
                    'CodeSystemName': 'SNOMED CT',
                    'Name': 'Shortness of Breath',
                    'Severity': {
                        'Code': '6736007',
                        'CodeSystem': '2.16.840.1.113883.6.96',
                        'CodeSystemName': 'SNOMED CT',
                        'Name': 'Moderate'
                    },
                    'Text': None
                }
            ],
            'Severity': {
                'Code': '6736007',
                'CodeSystem': '2.16.840.1.113883.6.96',
                'CodeSystemName': 'SNOMED CT',
                'Name': 'Moderate'
            },
            'StartDate': None,
            'Status': {
                'Code': '55561003',
                'CodeSystem': '2.16.840.1.113883.6.96',
                'CodeSystemName': 'SNOMED CT',
                'Name': 'Active'
            },
            'Substance': {
                'Code': '2670',
                'CodeSystem': '2.16.840.1.113883.6.88',
                'CodeSystemName': 'RxNorm',
                'Name': 'Codeine'
            },
            'Type': {
                'Code': '419511003',
                'CodeSystem': '2.16.840.1.113883.6.96',
                'CodeSystemName': 'SNOMED CT',
                'Name': 'Propensity to adverse reaction to drug'
            }
        },
        {
            'Comment': None,
            'Criticality': {
                'Code': 'CRITU',
                'CodeSystem': '2.16.840.1.113883.5.1063',
                'CodeSystemName': 'ObservationValue',
                'Name': 'Unable to assess criticality'
            },
            'EndDate': None,
            'Reaction': [
                {
                    'Code': '247472004',
                    'CodeSystem': '2.16.840.1.113883.6.96',
                    'CodeSystemName': 'SNOMED CT',
                    'Name': 'Hives',
                    'Severity': {
                        'Code': '371923003',
                        'CodeSystem': '2.16.840.1.113883.6.96',
                        'CodeSystemName': 'SNOMED CT',
                        'Name': 'Mild to moderate'
                    },
                    'Text': None
                }
            ],
            'Severity': {
                'Code': '371923003',
                'CodeSystem': '2.16.840.1.113883.6.96',
                'CodeSystemName': 'SNOMED CT',
                'Name': 'Mild to moderate'
            },
            'StartDate': None,
            'Status': {
                'Code': '55561003',
                'CodeSystem': '2.16.840.1.113883.6.96',
                'CodeSystemName': 'SNOMED CT',
                'Name': 'Active'
            },
            'Substance': {
                'Code': '1191',
                'CodeSystem': '2.16.840.1.113883.6.88',
                'CodeSystemName': 'RxNorm',
                'Name': 'Aspirin'
            },
            'Type': {
                'Code': '419511003',
                'CodeSystem': '2.16.840.1.113883.6.96',
                'CodeSystemName': 'SNOMED CT',
                'Name': 'Propensity to adverse reaction to drug'
            }
        }
    ],
    'Encounters': [
        {
            'DateTime': '2012-08-06T04:00:00.000Z',
            'Diagnosis': [
                {
                    'Code': '233604007',
                    'CodeSystem': '2.16.840.1.113883.6.96',
                    'CodeSystemName': 'SNOMED CT',
                    'Name': 'Pneumonia'
                }
            ],
            'EndDateTime': None,
            'Identifiers': [
                {
                    'ID': '2376492',
                    'IDType': 'URMC Epic CSN'
                },
                {
                    'ID': '8237334',
                    'IDType': '1.35.829.5.238422.9.10'
                }
            ],
            'Locations': [
                {
                    'Address': {
                        'City': 'Portland',
                        'Country': 'US',
                        'State': 'OR',
                        'StreetAddress': '1002 Healthcare Dr',
                        'ZIP': '97266'
                    },
                    'Name': 'Community Health and Hospitals',
                    'Type': {
                        'Code': '1160-1',
                        'CodeSystem': '2.16.840.1.113883.6.259',
                        'CodeSystemName': 'HealthcareServiceLocation',
                        'Name': 'Urgent Care Center'
                    }
                }
            ],
            'Providers': [
                {
                    'Address': {
                        'City': None,
                        'Country': None,
                        'County': None,
                        'State': None,
                        'StreetAddress': None,
                        'ZIP': None
                    },
                    'Credentials': [],
                    'FirstName': None,
                    'ID': None,
                    'IDType': None,
                    'LastName': None,
                    'Location': {
                        'Department': None,
                        'Facility': None,
                        'Room': None,
                        'Type': None
                    },
                    'PhoneNumber': {
                        'Office': None
                    },
                    'Role': {
                        'Code': '59058001',
                        'CodeSystem': '2.16.840.1.113883.6.96',
                        'CodeSystemName': 'SNOMED CT',
                        'Name': 'General Physician'
                    }
                }
            ],
            'ReasonForVisit': [
                {
                    'Code': '233604007',
                    'CodeSystem': '2.16.840.1.113883.6.96',
                    'CodeSystemName': 'SNOMED CT',
                    'Name': 'Pneumonia'
                }
            ],
            'Type': {
                'Code': '99222',
                'CodeSystem': '2.16.840.1.113883.6.12',
                'CodeSystemName': 'CPT',
                'Name': 'InPatient Admission'
            }
        }
    ],
    'FamilyHistory': [
        {
            'Problems': [
                {
                    'AgeAtOnset': '57',
                    'Code': '22298006',
                    'CodeSystem': '2.16.840.1.113883.6.96',
                    'CodeSystemName': 'SNOMED CT',
                    'DateTime': None,
                    'IsCauseOfDeath': None,
                    'Name': 'Myocardial infarction',
                    'Type': {
                        'Code': '55561003',
                        'CodeSystem': '2.16.840.1.113883.6.96',
                        'CodeSystemName': 'SNOMED CT',
                        'Name': 'Active'
                    }
                },
                {
                    'AgeAtOnset': '40',
                    'Code': '46635009',
                    'CodeSystem': '2.16.840.1.113883.6.96',
                    'CodeSystemName': 'SNOMED CT',
                    'DateTime': '1994-01-01T05:00:00.000Z',
                    'IsCauseOfDeath': None,
                    'Name': 'Diabetes mellitus type 1',
                    'Type': {
                        'Code': '7087005',
                        'CodeSystem': '2.16.840.1.113883.6.96',
                        'CodeSystemName': 'SNOMED CT',
                        'Name': 'Intermittent'
                    }
                }
            ],
            'Relation': {
                'Code': 'FTH',
                'CodeSystem': '2.16.840.1.113883.5.111',
                'CodeSystemName': 'HL7 FamilyMember',
                'Demographics': {
                    'DOB': '1912-01-01',
                    'Sex': 'Male'
                },
                'IsDeceased': True,
                'Name': 'Father'
            }
        }
    ],
    'Header': {
        'Document': {
            'Author': {
                'Address': {
                    'City': 'Madison',
                    'Country': 'USA',
                    'County': 'Dane',
                    'State': 'WI',
                    'StreetAddress': '123 Main St.',
                    'ZIP': '53703'
                },
                'Credentials': [
                    'MD'
                ],
                'FirstName': 'Pat',
                'ID': '4356789876',
                'IDType': 'NPI',
                'LastName': 'Granite',
                'Location': {
                    'Department': None,
                    'Facility': None,
                    'Room': None,
                    'Type': None
                },
                'PhoneNumber': {
                    'Office': '+16085551234'
                },
                'Type': None
            },
            'DateTime': '2012-09-12T00:00:00.000Z',
            'ID': '75cb4ad4-e5f9-4cd3-8750-eb5050521e0d',
            'Locale': 'US',
            'Title': 'Community Health and Hospitals: Health Summary',
            'Type': 'Summarization of Episode Note',
            'Visit': {
                'EndDateTime': '2018-05-06T03:32:53.157Z',
                'Location': {
                    'Department': '3N',
                    'Facility': 'RES General Hospital',
                    'Room': '136',
                    'Type': 'Inpatient'
                },
                'Reason': 'Annual Physical',
                'StartDateTime': '2018-05-06T03:32:53.157Z'
            }
        },
        'Patient': {
            'Demographics': {
                'Address': {
                    'City': 'Monroe',
                    'Country': 'US',
                    'County': 'Green',
                    'State': 'WI',
                    'StreetAddress': '4762 Hickory Street',
                    'ZIP': '53566'
                },
                'DOB': '2008-01-06',
                'EmailAddresses': [],
                'Ethnicity': None,
                'FirstName': 'Timothy',
                'LastName': 'Bixby',
                'MaritalStatus': 'Single',
                'PhoneNumber': {
                    'Home': '+18088675301',
                    'Mobile': None
                },
                'Race': 'Asian',
                'Religion': None,
                'SSN': '101-01-0001',
                'Sex': 'Male'
            },
            'Identifiers': [
                {
                    'ID': '0000000001',
                    'IDType': 'MR',
                    'Type': None
                },
                {
                    'ID': 'e167267c-16c9-4fe3-96ae-9cff5703e90a',
                    'IDType': 'EHRID',
                    'Type': None
                },
                {
                    'ID': 'a1d4ee8aba494ca',
                    'IDType': 'NIST',
                    'Type': None
                }
            ]
        }
    },
    'Immunizations': [
        {
            'DateTime': '2012-05-10T04:00:00.000Z',
            'Dose': {
                'Quantity': '50',
                'Units': 'mcg'
            },
            'Product': {
                'Code': '88',
                'CodeSystem': '2.16.840.1.113883.6.59',
                'CodeSystemName': 'CVX',
                'LotNumber': None,
                'Manufacturer': 'Health LS - Immuno Inc.',
                'Name': 'Influenza virus vaccine'
            },
            'Route': {
                'Code': 'C28161',
                'CodeSystem': '2.16.840.1.113883.3.26.1.1',
                'CodeSystemName': 'National Cancer Institute (NCI) Thesaurus',
                'Name': 'Intramuscular injection'
            }
        },
        {
            'DateTime': '2012-04-01T04:00:00.000Z',
            'Dose': {
                'Quantity': '50',
                'Units': 'mcg'
            },
            'Product': {
                'Code': '103',
                'CodeSystem': '2.16.840.1.113883.6.59',
                'CodeSystemName': 'CVX',
                'LotNumber': None,
                'Manufacturer': 'Health LS - Immuno Inc.',
                'Name': 'Tetanus and diphtheria toxoids - preservative free'
            },
            'Route': {
                'Code': 'C28161',
                'CodeSystem': '2.16.840.1.113883.3.26.1.1',
                'CodeSystemName': 'National Cancer Institute (NCI) Thesaurus',
                'Name': 'Intramuscular injection'
            }
        }
    ],
    'Insurances': [
        {
            'AgreementType': None,
            'Company': {
                'Address': {
                    'City': 'Lexington',
                    'Country': 'US',
                    'County': 'Fayette',
                    'State': 'KY',
                    'StreetAddress': 'PO Box 14080',
                    'ZIP': '40512-4079'
                },
                'ID': '60054',
                'IDType': None,
                'Name': 'aetna (60054 0131)',
                'PhoneNumber': '+18089541123'
            },
            'CoverageType': None,
            'EffectiveDate': '2015-01-01',
            'ExpirationDate': '2020-12-31',
            'GroupName': 'Accelerator Labs',
            'GroupNumber': '847025-024-0009',
            'Insured': {
                'Address': {
                    'City': None,
                    'Country': None,
                    'County': None,
                    'State': None,
                    'StreetAddress': None,
                    'ZIP': None
                },
                'DOB': None,
                'FirstName': None,
                'LastName': None,
                'Relationship': None,
                'Sex': None
            },
            'MemberNumber': None,
            'Plan': {
                'ID': '31572',
                'IDType': 'Payor ID',
                'Name': 'HMO Deductable Plan',
                'Type': None
            },
            'PolicyNumber': '9140860055'
        }
    ],
    'InsurancesText': None,
    'MedicalEquipment': [
        {
            'Product': {
                'Code': '72506001',
                'CodeSystem': '2.16.840.1.113883.6.96',
                'CodeSystemName': 'SNOMED CT',
                'Name': 'Automatic implantable cardioverter/defibrillator'
            },
            'Quantity': '2',
            'StartDate': '1999-11-01T05:00:00.000Z',
            'Status': 'completed'
        },
        {
            'Product': {
                'Code': '304120007',
                'CodeSystem': '2.16.840.1.113883.6.96',
                'CodeSystemName': 'SNOMED CT',
                'Name': 'Total hip replacement prosthesis'
            },
            'Quantity': None,
            'StartDate': '1998-01-01T05:00:00.000Z',
            'Status': 'completed'
        },
        {
            'Product': {
                'Code': '58938008',
                'CodeSystem': '2.16.840.1.113883.6.96',
                'CodeSystemName': 'SNOMED CT',
                'Name': 'Wheelchair'
            },
            'Quantity': None,
            'StartDate': '1999-01-01T05:00:00.000Z',
            'Status': 'completed'
        }
    ],
    'Medications': [
        {
            'Dose': {
                'Quantity': '4',
                'Units': 'mg'
            },
            'EndDate': None,
            'FreeTextSig': None,
            'Frequency': {
                'Period': '8',
                'Unit': 'h'
            },
            'IsPRN': None,
            'Prescription': False,
            'Product': {
                'Code': '104894',
                'CodeSystem': '2.16.840.1.113883.6.88',
                'CodeSystemName': 'RxNorm',
                'Name': 'Ondansetron 4 Mg Po Tbdp'
            },
            'Rate': {
                'Quantity': None,
                'Units': None
            },
            'Route': {
                'Code': 'C38288',
                'CodeSystem': '2.16.840.1.113883.3.26.1.1',
                'CodeSystemName': 'NCI Thesaurus',
                'Name': 'Oral'
            },
            'StartDate': '2013-11-11T05:00:00.000Z'
        },
        {
            'Dose': {
                'Quantity': '0.09',
                'Units': 'mg/actuat'
            },
            'EndDate': '2012-08-13T04:00:00.000Z',
            'FreeTextSig': None,
            'Frequency': {
                'Period': '12',
                'Unit': 'h'
            },
            'IsPRN': True,
            'Prescription': False,
            'Product': {
                'Code': '573621',
                'CodeSystem': '2.16.840.1.113883.6.88',
                'CodeSystemName': 'RxNorm',
                'Name': 'Albuterol 0.09 MG/ACTUAT inhalant solution'
            },
            'Rate': {
                'Quantity': '90',
                'Units': 'ml/min'
            },
            'Route': {
                'Code': 'C38216',
                'CodeSystem': '2.16.840.1.113883.3.26.1.1',
                'CodeSystemName': 'NCI Thesaurus',
                'Name': 'RESPIRATORY (INHALATION)'
            },
            'StartDate': '2012-08-06T04:00:00.000Z'
        }
    ],
    'Meta': {
        'DataModel': 'Clinical Summary',
        'Destinations': [
            {
                'ID': 'b49bc35b-726c-49c2-94c6-496311bdff13',
                'Name': 'Redox API Endpoint'
            }
        ],
        'EventDateTime': '2018-05-04T06:22:32.068Z',
        'EventType': 'PatientPush',
        'FacilityCode': None,
        'Message': {
            'ID': 5565
        },
        'Source': {
            'ID': '7ce6f387-c33c-417d-8682-81e83628cbd9',
            'Name': 'Redox Dev Tools'
        },
        'Test': True,
        'Transmission': {
            'ID': 252342454
        }
    },
    'PlanOfCare': {
        'Encounters': [
            {
                'Code': '99241',
                'CodeSystem': '2.16.840.1.113883.6.12',
                'CodeSystemName': 'CPT',
                'DateTime': '2012-08-20T05:00:00.000Z',
                'Name': 'Office consultation - 15 minutes',
                'Status': 'Intent'
            }
        ],
        'MedicationAdministration': [
            {
                'Dose': {
                    'Quantity': '81',
                    'Units': 'milliGRAM(s)'
                },
                'EndDate': '2012-10-31T04:59:00.000Z',
                'Frequency': {
                    'Period': None,
                    'Unit': None
                },
                'Product': {
                    'Code': '1191',
                    'CodeSystem': '2.16.840.1.113883.6.88',
                    'CodeSystemName': 'RxNorm',
                    'Name': 'aspirin'
                },
                'Rate': {
                    'Quantity': None,
                    'Units': None
                },
                'Route': {
                    'Code': 'C38288',
                    'CodeSystem': '2.16.840.1.113883.3.26.1.1',
                    'CodeSystemName': 'NCI Thesaurus',
                    'Name': 'ORAL'
                },
                'StartDate': '2012-10-02T05:00:00.000Z',
                'Status': 'Intent'
            }
        ],
        'Orders': [
            {
                'Code': '624-7',
                'CodeSystem': '2.16.840.1.113883.6.1',
                'CodeSystemName': None,
                'DateTime': '2012-08-20T05:00:00.000Z',
                'Name': 'Sputum Culture',
                'Status': 'Request'
            }
        ],
        'Procedures': [
            {
                'Code': '168731009',
                'CodeSystem': '2.16.840.1.113883.6.96',
                'CodeSystemName': 'SNOMED-CT',
                'DateTime': '2012-08-26T05:00:00.000Z',
                'Name': 'Chest X-Ray',
                'Status': 'Request'
            }
        ],
        'Services': [
            {
                'Code': '427519008',
                'CodeSystem': '2.16.840.1.113883.11.20.9.34',
                'CodeSystemName': 'patientEducationType',
                'DateTime': None,
                'Name': 'Caregiver',
                'Status': 'Intent'
            }
        ],
        'Supplies': []
    },
    'Problems': [
        {
            'Category': {
                'Code': '409586006',
                'CodeSystem': '2.16.840.1.113883.6.96',
                'CodeSystemName': 'SNOMED CT',
                'Name': 'Complaint'
            },
            'Code': '233604007',
            'CodeSystem': '2.16.840.1.113883.6.96',
            'CodeSystemName': 'SNOMED CT',
            'EndDate': '2012-08-06T04:00:00.000Z',
            'HealthStatus': {
                'Code': '162467007',
                'CodeSystem': '2.16.840.1.113883.6.96',
                'CodeSystemName': 'SNOMED CT',
                'Name': 'Symptom Free'
            },
            'Name': 'Pneumonia',
            'StartDate': '2012-08-06T04:00:00.000Z',
            'Status': {
                'Code': '413322009',
                'CodeSystem': '2.16.840.1.113883.6.96',
                'CodeSystemName': 'SNOMED CT',
                'Name': 'Resolved'
            }
        },
        {
            'Category': {
                'Code': '409586006',
                'CodeSystem': '2.16.840.1.113883.6.96',
                'CodeSystemName': 'SNOMED CT',
                'Name': 'Complaint'
            },
            'Code': '195967001',
            'CodeSystem': '2.16.840.1.113883.6.96',
            'CodeSystemName': 'SNOMED CT',
            'EndDate': '2012-08-06T04:00:00.000Z',
            'HealthStatus': {
                'Code': '162467007',
                'CodeSystem': '2.16.840.1.113883.6.96',
                'CodeSystemName': 'SNOMED CT',
                'Name': 'Symptom Free'
            },
            'Name': 'Asthma',
            'StartDate': '2007-10-17T04:00:00.000Z',
            'Status': {
                'Code': '55561003',
                'CodeSystem': '2.16.840.1.113883.6.96',
                'CodeSystemName': 'SNOMED CT',
                'Name': 'Active'
            }
        }
    ],
    'Procedures': {
        'Observations': [
            {
                'Code': '123456',
                'CodeSystem': '2.16.840.1.113883.6.96',
                'CodeSystemName': 'SNOMED-CT',
                'DateTime': '20120807',
                'Name': 'Fake observation',
                'Status': 'active',
                'TargetSite': {
                    'Code': '302539009',
                    'CodeSystem': '2.16.840.1.113883.6.96',
                    'CodeSystemName': 'SNOMED-CT',
                    'Name': 'Entire hand (body structure)'
                }
            }
        ],
        'Procedures': [
            {
                'Code': '168731009',
                'CodeSystem': '2.16.840.1.113883.6.96',
                'CodeSystemName': 'SNOMED-CT',
                'DateTime': '20120807',
                'Name': 'Chest X-Ray',
                'Status': 'completed',
                'TargetSite': {
                    'Code': '181608004',
                    'CodeSystem': '2.16.840.1.113883.6.96',
                    'CodeSystemName': 'SNOMED-CT',
                    'Name': 'Entire chest wall (body structure)'
                }
            }
        ],
        'Services': [
            {
                'Code': '123456',
                'CodeSystem': '2.16.840.1.113883.6.96',
                'CodeSystemName': 'SNOMED-CT',
                'DateTime': '20120807',
                'Name': 'Fake action',
                'Status': 'aborted'
            }
        ]
    },
    'Results': [
        {
            'Code': '43789009',
            'CodeSystem': '2.16.840.1.113883.6.96',
            'CodeSystemName': 'SNOMED CT',
            'Name': 'CBC WO DIFFERENTIAL',
            'Observations': [
                {
                    'Code': '30313-1',
                    'CodeSystem': '2.16.840.1.113883.6.1',
                    'CodeSystemName': 'LOINC',
                    'CodedValue': {
                        'Code': None,
                        'CodeSystem': None,
                        'CodeSystemName': None,
                        'Name': None
                    },
                    'DateTime': '2012-08-10T14:00:00.000Z',
                    'Interpretation': 'Normal',
                    'Name': 'HGB',
                    'ReferenceRange': {
                        'High': None,
                        'Low': None,
                        'Text': None
                    },
                    'Status': 'Final',
                    'Units': 'g/dl',
                    'Value': '10.2',
                    'ValueType': 'PhysicalQuantity'
                },
                {
                    'Code': '33765-9',
                    'CodeSystem': '2.16.840.1.113883.6.1',
                    'CodeSystemName': 'LOINC',
                    'CodedValue': {
                        'Code': None,
                        'CodeSystem': None,
                        'CodeSystemName': None,
                        'Name': None
                    },
                    'DateTime': '2012-08-10T14:00:00.000Z',
                    'Interpretation': 'Normal',
                    'Name': 'WBC',
                    'ReferenceRange': {
                        'High': None,
                        'Low': None,
                        'Text': None
                    },
                    'Status': 'Final',
                    'Units': '10+3/ul',
                    'Value': '12.3',
                    'ValueType': 'PhysicalQuantity'
                },
                {
                    'Code': '26515-7',
                    'CodeSystem': '2.16.840.1.113883.6.1',
                    'CodeSystemName': 'LOINC',
                    'CodedValue': {
                        'Code': None,
                        'CodeSystem': None,
                        'CodeSystemName': None,
                        'Name': None
                    },
                    'DateTime': '2012-08-10T14:00:00.000Z',
                    'Interpretation': 'Low',
                    'Name': 'PLT',
                    'ReferenceRange': {
                        'High': None,
                        'Low': None,
                        'Text': None
                    },
                    'Status': 'Final',
                    'Units': '10+3/ul',
                    'Value': '123',
                    'ValueType': 'PhysicalQuantity'
                }
            ],
            'Status': 'Final'
        },
        {
            'Code': '624-7',
            'CodeSystem': '2.16.840.1.113883.6.1',
            'CodeSystemName': 'LOINC',
            'Name': 'Sputum Culture',
            'Observations': [
                {
                    'Code': '86243-3',
                    'CodeSystem': '2.16.840.1.113883.6.1',
                    'CodeSystemName': 'LOINC',
                    'CodedValue': {
                        'Code': '54662009',
                        'CodeSystem': '2.16.840.1.113883.6.96',
                        'CodeSystemName': 'SNOMED CT',
                        'Name': 'Green'
                    },
                    'DateTime': '2012-08-10T14:00:00.000Z',
                    'Interpretation': None,
                    'Name': 'Color of Sputum',
                    'ReferenceRange': {
                        'High': None,
                        'Low': None,
                        'Text': None
                    },
                    'Status': 'Final',
                    'Units': None,
                    'Value': 'Green',
                    'ValueType': 'Code'
                }
            ],
            'Status': None
        }
    ],
    'SocialHistory': {
        'Observations': [
            {
                'Code': '160573003',
                'CodeSystem': '2.16.840.1.113883.6.96',
                'CodeSystemName': 'SNOMED CT',
                'EndDate': None,
                'Name': 'Alcohol Consumption',
                'StartDate': '1990-05-01T04:00:00.000Z',
                'Value': {
                    'Code': None,
                    'CodeSystem': None,
                    'CodeSystemName': None,
                    'Name': None
                },
                'ValueText': 'None'
            }
        ],
        'Pregnancy': [],
        'TobaccoUse': [
            {
                'Code': '8517006',
                'CodeSystem': '2.16.840.1.113883.6.96',
                'CodeSystemName': 'SNOMED CT',
                'EndDate': None,
                'IsSmokingStatus': True,
                'Name': 'Former smoker',
                'StartDate': '2015-06-03T09:35:00.000Z'
            },
            {
                'Code': '65568007',
                'CodeSystem': '2.16.840.1.113883.6.96',
                'CodeSystemName': 'SNOMED CT',
                'EndDate': '2008-09-01',
                'IsSmokingStatus': False,
                'Name': 'Cigarette smoker',
                'StartDate': '2005-05-01'
            }
        ]
    },
    'VitalSigns': [
        {
            'DateTime': '1999-11-14T00:00:00.000Z',
            'Observations': [
                {
                    'Code': '8302-2',
                    'CodeSystem': '2.16.840.1.113883.6.1',
                    'CodeSystemName': 'LOINC',
                    'DateTime': '1999-11-14T00:00:00.000Z',
                    'Interpretation': 'Normal',
                    'Name': 'Height',
                    'Status': 'completed',
                    'Units': 'cm',
                    'Value': '177'
                },
                {
                    'Code': '3141-9',
                    'CodeSystem': '2.16.840.1.113883.6.1',
                    'CodeSystemName': 'LOINC',
                    'DateTime': '1999-11-14T00:00:00.000Z',
                    'Interpretation': 'Normal',
                    'Name': 'Patient Body Weight - Measured',
                    'Status': 'completed',
                    'Units': 'kg',
                    'Value': '86'
                },
                {
                    'Code': '8480-6',
                    'CodeSystem': '2.16.840.1.113883.6.1',
                    'CodeSystemName': 'LOINC',
                    'DateTime': '1999-11-14T00:00:00.000Z',
                    'Interpretation': 'Normal',
                    'Name': 'Intravascular Systolic',
                    'Status': 'completed',
                    'Units': 'mm[Hg]',
                    'Value': '132'
                }
            ]
        },
        {
            'DateTime': '2000-04-07T00:00:00.000Z',
            'Observations': [
                {
                    'Code': '8302-2',
                    'CodeSystem': '2.16.840.1.113883.6.1',
                    'CodeSystemName': 'LOINC',
                    'DateTime': '2000-04-07T00:00:00.000Z',
                    'Interpretation': 'Normal',
                    'Name': 'Height',
                    'Status': 'completed',
                    'Units': 'cm',
                    'Value': '177'
                },
                {
                    'Code': '3141-9',
                    'CodeSystem': '2.16.840.1.113883.6.1',
                    'CodeSystemName': 'LOINC',
                    'DateTime': '2000-04-07T00:00:00.000Z',
                    'Interpretation': 'Normal',
                    'Name': 'Patient Body Weight - Measured',
                    'Status': 'completed',
                    'Units': 'kg',
                    'Value': '88'
                },
                {
                    'Code': '8480-6',
                    'CodeSystem': '2.16.840.1.113883.6.1',
                    'CodeSystemName': 'LOINC',
                    'DateTime': '2000-04-07T00:00:00.000Z',
                    'Interpretation': 'Normal',
                    'Name': 'Intravascular Systolic',
                    'Status': 'completed',
                    'Units': 'mm[Hg]',
                    'Value': '145'
                }
            ]
        }
    ]
}
