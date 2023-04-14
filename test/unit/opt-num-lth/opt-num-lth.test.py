#!/usr/bin/python

import os, ultraimport
ultraimport('__dir__/../../tester.py', '*', locals())

def prep_input(input):
    return [ubyte(input[0]), us(input[1])]

# Given that a string is saved in memory
# When opt-num-lth is called with the address of the string and a limit (exclusive)
# Then it returns True if 
    # the arg is not empty and
    # all chars are digits and
    # no leading 0s, unless the input is 0
    # number < limit
def main():
    t = Tester(__file__)

    max_lim = 255    
    passes = [
        ['limit > input', [3, 1]],
        ['limit > 0', [3, 0]],
        ['max limit > 0', [max_lim, 0]],
        ['max limit > limit - 1', [max_lim, 254]],
        ['non-leading 0', [max_lim, 100]],
        ['non-leading 0 (2)', [max_lim, 101]],
    ]  

    fails = [
        ['limit = input', [max_lim, 255]],
        ['limit = input (2)', [0, 0]],
        ['limit = input (3)', [3, 3]],
        ['non-numeric input', [3, 'a']],
        ['non-numeric input (2)', [max_lim, '1a']],
        ['non-0 limit with empty input', [3, '']],
        ['0 limit with empty input', [0, '']],
        ['input 00', [3, '00']],
        ['input 000', [3, '000']],
        ['input 000000', [3, '000000']],
        ['input with 1 leading 0', [5, '02']],
        ['input with 2 leading 0s', [5, '002']],
        ['input with 3 leading 0s', [5, '0002']],
        ['input > limit', [3, 4]],
        ['input max num, limit max', [max_lim, MAX_NUM]],
        ['input > max num, limit max', [max_lim, MAX_NUM * 10]],
    ]

    for case in passes:
        t.test(case[0], prep_input(case[1]), ubyte(True)) 

    for case in fails:
        t.test(case[0], prep_input(case[1]), ubyte(False)) 

    t.done()    


if __name__ == "__main__":
    main()
