# prescription refill path
prStateMap = {
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
			'next-state': 'pr-refill'
		},
		'no': {
			'next-state': 'pr-refill-no'
		}
	},
	'pr-refill': {
		'text-template': 'pr-refill'
	},
	'pr-refill-no': {
		'text-template': 'pr-refill-no'
	}
	

}
