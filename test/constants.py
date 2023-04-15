#!/usr/bin/python

# system constants
MAX_NUM = (1 << 32) - 1
VOTES_LEN = 1020
MAX_COMMAND_NAME_LEN = 12
INPUT_LEN = 2817
MAX_OPT_NUM = (1 << 8) - 1
MAX_CAND = MAX_OPT_NUM - 1
DEFAULT_CAND = 2

NL = '\n'

# commands
setup_x = lambda x: f'setup {x}'
start_vote = 'start vote'
end_vote = 'end vote'
next_voter = 'next voter'
vote_x = lambda x: f'vote {x}'
add_results_x = lambda x: f'add results {x}'
tabulate = 'tabulate'

# outputs
vote_in_progress = 'Vote currently in progress' + NL
no_vote_in_progress = 'No vote in progress' + NL
command_not_rec = 'Command not recognised' + NL
vote_cast = 'Vote cast' + NL
invalid_cand_num = 'Invalid candidate number provided' + NL
invalid_setup_arg = 'Invalid number of candidates provided' + NL
setup_arg_too_small = 'Number of candidates must be at least 2' + NL
invalid_results = 'Invalid vote results provided' + NL
not_ready = 'Not ready for next voter' + NL
cand_set_x = lambda o: f'Number of candidates set to: {o}' + NL
def results_x(counts):
	invalid = f'Invalid votes: {counts.pop(0)}{NL}'
	rest= ''.join([f'Votes for candidate {i + 1}: {c}{NL}' for i, c in enumerate(counts)])
	return invalid + rest

prompt = '>> '
welcome = 'Welcome to `pebble`!\n' + cand_set_x(DEFAULT_CAND)
