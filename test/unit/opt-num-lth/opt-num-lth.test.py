#!/usr/bin/python

import os, ultraimport
ultraimport('__dir__/../../tester.py', '*', locals())

def prep_input(input):
    return [ushort(input[0]), us(input[1])]

# Given that a string is saved in memory
# When opt-num-lth is called with the address of the string and a limit (exclusive)
# Then it returns True if 
    # the arg is not empty and
    # all chars are digits and
    # no leading 0s, unless the input is 0
    # number < limit
def main():
    t = Tester(__file__)

    LAST_OPT = MAX_OPT_LEN - 1
    MAX_LIM = (1 << 16) - 1
    passes = [
        ['3 > 1', [3, 1]],
        ['3 > 0', [3, 0]],
        ['max number of options > 0', [MAX_OPT_LEN, 0]],
        ['max number of options > last valid option', [MAX_OPT_LEN, LAST_OPT]],
        ['last valid option > last valid option - 1', [LAST_OPT, LAST_OPT - 1]],
        ['non-leading 0', [LAST_OPT, 100]],
        ['non-leading 0', [LAST_OPT, 101]],
    ]  

    fails = [
        ['limit = input', [LAST_OPT, LAST_OPT]],
        ['limit = input (2)', [MAX_OPT_LEN, MAX_OPT_LEN]],
        ['non-numeric input', [3, 'a']],
        ['non-numeric input (2)', [LAST_OPT, '1a']],
        ['non-0 limit with empty input', [3, '']],
        ['0 limit with empty input', [0, '']],
        ['input 00', [3, '00']],
        ['input 000', [3, '000']],
        ['input 000000', [3, '000000']],
        ['input with 1 leading 0', [5, '02']],
        ['input with 2 leading 0s', [5, '002']],
        ['input with 3 leading 0s', [5, '0002']],
        ['input > limit', [3, 4]],
        ['input max num, limit ffff', [MAX_LIM, MAX_NUM]],
        ['input > max num, limit ffff', [MAX_LIM, MAX_NUM * 10]],
    ]

    for case in passes:
        t.test(case[0], prep_input(case[1]), ubyte(True)) 

    for case in fails:
        t.test(case[0], prep_input(case[1]), ubyte(False)) 

    t.done()    


if __name__ == "__main__":
    main()
