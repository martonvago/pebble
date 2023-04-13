#!/usr/bin/python

import os, ultraimport
ultraimport('__dir__/../../tester.py', '*', locals())

# Given that the args of the add-results command are saved in memory
# When prep-arg is called with the address of the first char and the array cap
# Then it returns True if the string is well-formed
    # contains only digits or semicolon
    # starts with digit
    # ends with semicolon or digit
    # no two consecutive semicolons
def main():
    t = Tester(__file__)
   
    passes = [
        ['array full: no ; at arg end', ['0005', '"1;2;3']],
        ['array not full: no ; at arg end', ['0006', '"1;2;3 00']],
        ['array full: ; at arg end', ['0006', '"1;2;3;']],
        ['array not full: ; at arg end', ['0007', '"1;2;3; 00']],
        ['empty array', ['0004', '00 00 00 00']],
        ['0-length array', ['0000', '']],
        ['1-length array', ['0001', '"0']],
        ['array with multi-digit numbers', ['0018', '"00023;12321;0;12;1232 00 00 00']],
        [
            'maximum add-results arg', 
            [format(INPUT_LEN - MAX_COMMAND_NAME_LEN, '04x'), us(f'{MAX_NUM};' * MAX_OPTIONS)[:-3]], 
        ],
    ]

    fails = [
        ['non-digit', ['0001', '"a']],
        ['non-digit (2)', ['0007', '"1;2;w;3']],
        ['; at start', ['0001', '";']],
        ['; at start (2)', ['0002', '";0']],
        ['double ;', ['0002', '";;']],
        ['double ; (2)', ['0003', '"1;;']],
        ['double ; (3)', ['0004', '"1;;2']],
        ['leading 00s', ['0005', '00 00 "1;2']],
    ]

    for case in passes:
        t.test(*case, ubyte(True)) 

    for case in fails:
        t.test(*case, ubyte(False)) 

    t.done()    


if __name__ == "__main__":
    main()
