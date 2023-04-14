#!/usr/bin/python

import ultraimport
ultraimport('__dir__/../tester.py', '*', locals())

def main():
    LONG_WAIT = 2

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
    results_x = lambda counts: ''.join([f'Votes for candidate {i}: {c}{NL}' for i, c in enumerate(counts)])
    cand_set_x = lambda o: f'Number of candidates set to: {o}' + NL

    t = Tester(__file__)

    # input
    t.interact('empty input not allowed', [''], command_not_rec)
    t.interact('input > buffer not allowed', ['a' * (INPUT_LEN + 1)], command_not_rec)
    t.interact('input > buffer not allowed (2)', [start_vote + 'x' * (INPUT_LEN + 1 - len(start_vote))], command_not_rec)
    t.interact('input > buffer not allowed (3)', [start_vote + ' ' * (INPUT_LEN + 1 - len(start_vote))], command_not_rec)
    t.interact('unknown command not allowed', ['hello'], command_not_rec)
    t.interact('unknown command not allowed (2)', ['start-vote'], command_not_rec)
    t.interact('max-length input allowed', [setup_x(MAX_CAND), add_results_x(f'{MAX_NUM};' * MAX_OPT_NUM)], cand_set_x(MAX_CAND))

    # setup
    ## args
    t.interact('setup must have args', ['setup'], command_not_rec)
    t.interact('setup must have args (2)', ['setup '], command_not_rec)
    t.interact('setup arg must be numeric', [setup_x('a')], invalid_setup_arg)
    t.interact('setup arg must be numeric (2)', [setup_x('1a')], invalid_setup_arg)
    t.interact('setup arg cannot be 0', [setup_x(0)], setup_arg_too_small)
    t.interact('setup arg cannot be 1', [setup_x(1)], setup_arg_too_small)
    t.interact('setup arg can be 2', [setup_x(2)], cand_set_x(2))
    t.interact('setup arg must not have leading 0s', [setup_x('00')], invalid_setup_arg)
    t.interact('setup arg must not have leading 0s (2)', [setup_x('01')], invalid_setup_arg)
    t.interact(f'setup arg cannot be > {MAX_CAND}', [setup_x(MAX_CAND + 1)], invalid_setup_arg)
    t.interact(f'setup arg can be {MAX_CAND}', [setup_x(MAX_CAND)], cand_set_x(MAX_CAND))

    ## behaviour
    t.interact('setup illegal when voting', [start_vote, setup_x(3)], vote_in_progress)
    t.interact('setup illegal when voting (2)', [start_vote, vote_x(1), setup_x(3)], vote_cast + vote_in_progress)
    t.interact('setup illegal when voting (3)', [start_vote, vote_x(1), next_voter, setup_x(3)], vote_cast + vote_in_progress)
    t.interact('setup legal twice in a row', [setup_x(3), setup_x(5)], cand_set_x(3) + cand_set_x(5))
    t.interact(
        'changing number of candidates has effect', 
        [setup_x(3), start_vote, vote_x(4), end_vote, setup_x(7), start_vote, vote_x(4)], 
        cand_set_x(3) + invalid_cand_num + cand_set_x(7) + vote_cast
    )
    t.interact(
        'setup resets counts', 
        [add_results_x('2;3;4'), tabulate, setup_x(5), tabulate], 
        results_x([2, 3, 4]) + cand_set_x(5) + results_x([0] * 6)
    )

    # start vote
    t.interact(f'`{start_vote}` allows no args', [start_vote + 'abcd'], command_not_rec)
    t.interact(f'`{start_vote}` allows no args (2)', [start_vote + ' '], command_not_rec)
    t.interact(f'`{start_vote}` starts vote', [start_vote], '')
    t.interact(f'`{start_vote}` illegal twice in a row', [start_vote, start_vote], vote_in_progress)
    t.interact(f'`{start_vote}` illegal after casting vote', [start_vote, vote_x(1), start_vote], vote_cast + vote_in_progress)
    t.interact(f'`{start_vote}` illegal after next voter', [start_vote, vote_x(1), next_voter, start_vote], vote_cast + vote_in_progress)
    t.interact(f'`{start_vote}` legal after `{end_vote}`', [start_vote, end_vote, start_vote], '')
    t.interact(f'`{start_vote}` legal after `{end_vote}` (100x)', [start_vote, end_vote] * 100, '')
    
    # end vote
    t.interact(f'`{end_vote}` allows no args', [start_vote, end_vote + 'abcd'], command_not_rec)
    t.interact(f'`{end_vote}` allows no args (2)', [start_vote, end_vote + ' '], command_not_rec)
    t.interact(f'`{end_vote}` illegal when not voting', [end_vote], no_vote_in_progress)
    t.interact(f'`{end_vote}` illegal twice in a row', [start_vote, end_vote, end_vote], no_vote_in_progress)
    t.interact(f'`{end_vote}` ends vote', [start_vote, end_vote], '')

    # next voter
    t.interact(f'`{next_voter}` allows no args', [start_vote, next_voter + 'abcd'], command_not_rec)
    t.interact(f'`{next_voter}` allows no args (2)', [start_vote, next_voter + ' '], command_not_rec)
    t.interact(f'`{next_voter}` illegal when not voting', [next_voter], no_vote_in_progress)
    t.interact(f'`{next_voter}` illegal when not voting (2)', [start_vote, end_vote, next_voter], no_vote_in_progress)
    t.interact(f'`{next_voter}` legal twice in a row (no votes)', [start_vote, next_voter, next_voter], '')
    t.interact(f'`{next_voter}` legal twice in a row (with votes)', [start_vote, vote_x(1), next_voter, next_voter, vote_x(1)], vote_cast * 2)
    t.interact(f'`{next_voter}` re-enables voting after vote', [start_vote, vote_x(1), vote_x(1), next_voter, vote_x(1)], vote_cast + not_ready + vote_cast)
    t.interact(f'`{next_voter}` re-enables voting after vote (100x)', [start_vote, *[vote_x(1), vote_x(1), next_voter] * 100], (vote_cast + not_ready) * 100, LONG_WAIT)

    # vote
    ## args
    t.interact('vote must have args', [start_vote, 'vote'], command_not_rec)
    t.interact('vote must have args (2)', [start_vote, 'vote '], command_not_rec)
    t.interact('vote arg must be numeric', [start_vote, vote_x('a')], invalid_cand_num)
    t.interact('vote arg must be numeric (2)', [start_vote, vote_x('1a')], invalid_cand_num)
    t.interact('vote arg can be 0', [start_vote, vote_x(0)], vote_cast)
    t.interact('vote arg must not have leading 0s', [start_vote, vote_x('00')], invalid_cand_num)
    t.interact('vote arg must not have leading 0s (2)', [start_vote, vote_x('01')], invalid_cand_num)
    t.interact('vote arg cannot be > last candidate number', [setup_x(6), start_vote, vote_x(7)], cand_set_x(6) + invalid_cand_num)
    t.interact('vote arg can be = last candidate number', [setup_x(6), start_vote, vote_x(6)], cand_set_x(6) + vote_cast)
    t.interact('vote arg can be < last candidate number', [setup_x(6), start_vote, vote_x(5)], cand_set_x(6) + vote_cast)

    ## behaviour
    t.interact('vote illegal when not voting', [vote_x(1), tabulate], no_vote_in_progress + results_x([0, 0, 0]))
    t.interact('vote illegal when not voting (2)', [start_vote, end_vote, vote_x(1), tabulate], no_vote_in_progress + results_x([0, 0, 0]))
    t.interact('vote illegal twice in a row in same election', [start_vote, vote_x(1), vote_x(1), end_vote, tabulate], vote_cast + not_ready + results_x([0, 1, 0]))
    t.interact('vote legal twice in a row in different elections', [start_vote, vote_x(1), end_vote, start_vote, vote_x(1)], vote_cast * 2)
    t.interact('vote places vote on given option', [start_vote, vote_x(0), end_vote, tabulate], vote_cast + results_x([1, 0, 0]))
    t.interact('vote places vote on given option (2)', [start_vote, vote_x(1), end_vote, tabulate], vote_cast + results_x([0, 1, 0]))
    t.interact('vote places vote on given option (3)', [start_vote, vote_x(2), end_vote, tabulate], vote_cast + results_x([0, 0, 1]))
    
    # tabulate
    t.interact(f'`{tabulate}` allows no args', [tabulate + 'abcd'], command_not_rec)
    t.interact(f'`{tabulate}` allows no args (2)', [tabulate + ' '], command_not_rec)
    t.interact(f'`{tabulate}` illegal when voting', [start_vote, tabulate], vote_in_progress)
    t.interact(f'`{tabulate}` illegal when voting (2)', [start_vote, vote_x(1), tabulate], vote_cast + vote_in_progress)
    t.interact(f'`{tabulate}` illegal when voting (3)', [start_vote, vote_x(1), next_voter, tabulate], vote_cast + vote_in_progress)
    t.interact(f'`{tabulate}` legal twice in a row', [tabulate, tabulate], results_x([0, 0, 0]) * 2)
    t.interact(f'`{tabulate}` shows vote counts', [start_vote, vote_x(1), end_vote, tabulate], vote_cast + results_x([0, 1, 0]))

    # add results
    ## args
    t.interact('add results must have args', ['add results'], command_not_rec)
    t.interact('add results must have args (2)', ['add results '], command_not_rec)
    t.interact('add results arg can contain only digits and ;', [add_results_x('a;b;c')], invalid_results)
    t.interact('add results arg can contain only digits and ; (2)', [add_results_x('1;a;2')], invalid_results)
    t.interact('add results arg must start with a digit', [add_results_x(';1;2;3')], invalid_results)
    t.interact('add results arg must not contain 2 consecutive ;s', [add_results_x('1;;2;3')], invalid_results)
    t.interact('add results arg cannot have fewer numbers than option number', [add_results_x('1;2;')], invalid_results)
    t.interact('add results arg cannot have more numbers than option number', [add_results_x('1;2;3;4')], invalid_results)
    t.interact('add results arg cannot have number > ffff ffff', [add_results_x(f'1;2;{MAX_NUM + 1};')], invalid_results)
    
    t.interact('add results arg can end with digit', [add_results_x('1;2;3')], '')
    t.interact('add results arg can end with ;', [add_results_x('1;2;3;')], '')
    t.interact('add results arg can have leading 0s', [add_results_x('001;02;00003;')], '')
    t.interact('add results arg can have ffff ffff', [add_results_x(f'{MAX_NUM};{MAX_NUM};{MAX_NUM};')], '')

    ## behaviour
    t.interact('add results illegal when voting', [start_vote, add_results_x('1;2;3'), end_vote, tabulate], vote_in_progress + results_x([0, 0, 0]))
    t.interact('add results illegal when voting (2)', [start_vote, vote_x(1), add_results_x('1;2;3')], vote_cast + vote_in_progress)
    t.interact('add results illegal when voting (3)', [start_vote, vote_x(1), next_voter, add_results_x('1;2;3')], vote_cast + vote_in_progress)
    
    t.interact('add results legal twice in a row', [add_results_x('1;2;3'), add_results_x('1;2;3')], '')
    t.interact('add results adds results correctly', [tabulate, add_results_x('1;2;3'), tabulate], results_x([0, 0, 0]) + results_x([1, 2, 3]))
    t.interact('add results adds max num correctly', [add_results_x(f'{MAX_NUM};{MAX_NUM};{MAX_NUM};'), tabulate], results_x([MAX_NUM, MAX_NUM, MAX_NUM]))
    t.interact('add results adds twice in a row correctly', [add_results_x('1;2;3'), add_results_x('1;2;3'), tabulate], results_x([2, 4, 6]))
    t.interact('add results adds 100x in a row correctly', [*[add_results_x('1;2;3')] * 100, tabulate], results_x([100, 200, 300]), LONG_WAIT)

    # full runs
    t.interact('full voting subroutine', [start_vote, vote_x(1), next_voter, vote_x(1), end_vote, tabulate], vote_cast * 2 + results_x([0, 2, 0]))
    t.interact(f'full voting subroutine, ending with {next_voter}', [start_vote, vote_x(1), next_voter, vote_x(1), next_voter, end_vote, tabulate], vote_cast * 2 + results_x([0, 2, 0]))
    t.interact(
        'full voting subroutine (1000 votes)', 
        [start_vote, *[vote_x(1), next_voter] * 1000, end_vote, tabulate, add_results_x('12334;432;767654'), tabulate], 
        vote_cast * 1000 + results_x([0, 1000, 0]) + results_x([12334, 1432, 767654]), 
        LONG_WAIT
    )
    
    varied_votes = [vote_x(0), next_voter, vote_x(2), next_voter, vote_x(1), next_voter] * 333
    varied_votes2 = [vote_x(0), next_voter, vote_x(0), next_voter, vote_x(1), next_voter] * 333
    t.interact('full voting subroutine (varied votes)', [start_vote, *varied_votes, end_vote, tabulate], vote_cast * 999 + results_x([333, 333, 333]), LONG_WAIT)
    t.interact(
        'full voting subroutine (varied votes 2)', 
        [start_vote, *varied_votes2, end_vote, tabulate, add_results_x('12334;432;767654'), tabulate], 
        vote_cast * 999 + results_x([666, 333, 0]) + results_x([13000, 765, 767654]), 
        LONG_WAIT
    )
  
    t.interact(
        f'`{start_vote}` resets the counters', 
        [start_vote, vote_x(1), next_voter, vote_x(1), end_vote, tabulate, start_vote, end_vote, tabulate], 
        vote_cast * 2 + results_x([0, 2, 0]) + results_x([0, 0, 0])
    )
    t.interact(
        f'`{start_vote}` resets the counters after adding results', 
        [add_results_x('1;2;3'), tabulate, start_vote, end_vote, tabulate], 
        results_x([1, 2, 3]) + results_x([0, 0, 0])
    )

    t.interact(
        'multiple elections in a row with different number of options',
        [setup_x(10), start_vote, vote_x(5), next_voter, vote_x(22), vote_x(0), end_vote, tabulate,
        setup_x(4), start_vote, vote_x(5), vote_x(0), vote_x(0), next_voter, vote_x(1), end_vote, tabulate],
        cand_set_x(10) + vote_cast + invalid_cand_num + vote_cast + results_x([1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]) +
        cand_set_x(4) + invalid_cand_num + vote_cast + not_ready + vote_cast + results_x([1, 1, 0, 0, 0])
    )

    t.done()    


if __name__ == "__main__":
    main()
