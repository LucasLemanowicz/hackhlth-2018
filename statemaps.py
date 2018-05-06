# blood pressure path
bpStateMap = {
    'bp-welcome-greeting': {
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

# prescription refill path
