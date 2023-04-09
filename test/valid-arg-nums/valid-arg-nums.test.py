#!/usr/bin/python

import sys, os, ultraimport
ultraimport('__dir__/../tester.py', '*', locals())

def to_ascii_array(nums):
    return uarray([to_ascii_code(n) for n in nums])

def prep_input(input):
    return [ubyte_lit(input[0]), to_ascii_array(input[1])]

# Given that the args of the add-results command are 
    # saved in memory and 
    # are well-formed and
    # have been parsed into an array (of decimal strings) and
    # the number of vote options is set [01, ff] and
# When valid-arg-nums is called with the address of the first element and the option number
# Then it returns True if 
    # all the numbers are representable in 32 bits and
    # the number of elements equals the number of options
def main():
    t = Tester(__file__)

    passes = [
        ['single option', [1, [1]]],
        ['single option with 0 votes', [1, [0]]],
        ['single option with max vote count', [1, [MAX_NUM]]],
        ['multiple options', [3, [1, 2, 3]]],
        ['vote counts with leading 0s', [3, ['00000001', '002', '03']]],
        ['higher vote counts', [3, [2343, 0, 124234]]],
        ['max options', [255, [23] * 255]],
        ['max options with 0 votes', [255, [0] * 255]],
        ['max options with max vote count for each', [255, [MAX_NUM] * 255]],
    ]  

    fails = [
        ['too many vote counts', [1, [1, 2, 3]]],
        ['too few vote counts', [9, [1, 2, 3]]],
        ['vote count too large', [3, [1, MAX_NUM + 1, 3]]],
        ['max options with vote count too large for each', [255, [MAX_NUM + 1] * 255]],
    ]

    for case in passes:
        t.test(case[0], prep_input(case[1]), ubyte(True)) 

    for case in fails:
        t.test(case[0], prep_input(case[1]), ubyte(False)) 

    sys.exit(t.fail)    


if __name__ == "__main__":
    main()
