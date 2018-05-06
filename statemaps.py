# Blood Pressure Path
BP_STATEMAP = {
    'welcome-greeting': {
        'text-template': 'bp-welcome-greeting',
        'yes': {
            'next-state': 'bp-measurement-yes',
        },
        'no': {
            'next-state': 'bp-check-in-later',
        }
    },
    'bp-check-in-later': {
        'text-template': 'bp-check-in-later'
    },
    'bp-measurement-yes': {
        'text-template': 'bp-measurement-yes',
        'next-state': 'bp-measurement-confirm'
    },
    'bp-measurement-confirm': {
        'text-template': 'bp-measurement-confirm',
        'yes': {
            'next-state': 'bp-aspirin-prompt',
        },
        'no': {
            'next-state': 'bp-measurement-again',
        }
    },
    'bp-measurement-again': {
        'text-template': 'bp-measurement-again',
        'next-state': 'bp-measurement-confirm'
    },
    'bp-aspirin-prompt': {
        'text-template': 'bp-aspirin-prompt',
        'yes': {
            'next-state': 'bp-yes-and-send-to-dr',
        },
        'no': {
            'next-state': 'bp-no-and-send-to-dr',
        }
    },
    'bp-yes-and-send-to-dr': {
        'text-template': 'bp-yes-and-send-to-dr',
        'yes': {
            'next-state': 'bp-thanks-and-good-bye',
        },
        'no': {
            'next-state': 'bp-okay-and-good-bye',
        }
    },
    'bp-no-and-send-to-dr': {
        'text-template': 'bp-no-and-send-to-dr',
        'yes': {
            'next-state': 'bp-thanks-and-good-bye',
        },
        'no': {
            'next-state': 'bp-okay-and-good-bye',
        }
    },
    'bp-okay-and-good-bye': {
        'text-template': 'bp-okay-and-good-bye'
    },
    'bp-thanks-and-good-bye': {
        'text-template': 'bp-thanks-and-good-bye'
    }
}

# Prescription Refill Path
PR_STATEMAP = {
    'welcome-greeting': {
        'text-template': 'pr-welcome-greeting',
        'yes': {
            'next-state': 'pr-pill-count-check'
        },
        'no': {
            'next-state': 'pr-will-check-again'
        }
    },
    'pr-pill-count-check': {
        'text-template': 'pr-pill-count-check',
        'next-state': 'pr-pill-count-confirmation'
    },
    'pr-will-check-again': {
        'text-template': 'pr-will-check-again',
    },
    'pr-pill-count-confirmation': {
        'text-template': 'pr-pill-count-confirmation',
        'yes': {
            'next-state': 'pr-card-check'
        },
        'no': {
            'next-state': 'pr-refill-no'
        }
    },
    'pr-card-check': {
        'text-template': 'pr-card-check',
        'yes': {
            'next-state': 'pr-refill'
        },
        'no': {
            'next-state': 'pr-card-check-no'
        }
    },
    'pr-card-check-no': {
        'text-template': 'pr-card-check-no',
    },
    'pr-refill': {
        'text-template': 'pr-refill'
    },
    'pr-refill-no': {
        'text-template': 'pr-refill-no'
    }
}
