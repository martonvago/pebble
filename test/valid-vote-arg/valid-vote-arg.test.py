#!/usr/bin/python

import sys, os, ultraimport
ultraimport('__dir__/../tester.py', '*', locals())

def prep_input(input):
    return [ubyte_lit(input[0]), us(input[1])]

# Given that the args of the vote command are saved in memory
# When valid-vote-arg is called with the address of the first element and the option number
# Then it returns True if 
    # the arg is not empty and
    # all chars are digits and
    # no leading 0s, unless the input is 0
    # number < number of options (with 0 indicating an invalid vote)
def main():
    t = Tester(__file__)

    MAX_OPT = (1 << 8) - 1
    passes = [
        ['min options', [3, 1]],
        ['max options with invalid vote', [MAX_OPT, 0]],
        ['max options with max vote', [MAX_OPT, MAX_OPT - 1]],
        ['zero', [3, '0']],
        ['non-leading 0', [MAX_OPT, 100]],
        ['non-leading 0', [MAX_OPT, 101]],
    ]  

    fails = [
        ['non-numeric arg', [3, 'a']],
        ['non-numeric arg 2', [MAX_OPT, '1a']],
        ['empty arg', [3, '']],
        ['00', [3, '00']],
        ['000', [3, '000']],
        ['000000', [3, '000000']],
        ['1 leading 0', [5, '02']],
        ['2 leading 0s', [5, '002']],
        ['3 leading 0s', [5, '0002']],
        ['arg > max vote option', [3, 3]],
        ['arg > max vote option 2', [3, 4]],
        ['arg > max vote option 3', [MAX_OPT, MAX_OPT]],
        ['arg > max vote option 4', [MAX_OPT, MAX_NUM]],
        ['arg > max vote option 5', [MAX_OPT, '999999999999999999999999999']],
    ]

    for case in passes:
        t.test(case[0], prep_input(case[1]), ubyte(True)) 

    for case in fails:
        t.test(case[0], prep_input(case[1]), ubyte(False)) 

    sys.exit(t.fail)    


if __name__ == "__main__":
    main()
