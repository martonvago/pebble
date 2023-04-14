#!/usr/bin/python

import os, ultraimport
ultraimport('__dir__/../../tester.py', '*', locals())

# Given that the args of the add-results command are saved in memory and are well-formed
# When prep-arg is called with the address of the first char and the array cap
# Then it replaces the semicolons with 00 terminators
def main():
    t = Tester(__file__)

    cases = [
        ['array full: no ; at arg end', ['0005', '"1;2;3'], '3100320033'],
        ['array not full: no ; at arg end', ['0006', '"1;2;3 00'], '310032003300'],
        ['array full: ; at arg end', ['0006', '"1;2;3;'], '310032003300'],
        ['array not full: ; at arg end', ['0007', '"1;2;3; 00'], '31003200330000'],
        ['0-length array', ['0000', ''], ''],
        ['array with multi-digit numbers', ['0018', '"00023;12321;0;12;1232 00 00 00'], '303030323300313233323100300031320031323332000000'],
        [
            'maximum add-results arg', 
            [format(INPUT_LEN - MAX_COMMAND_NAME_LEN, '04x'), us(f'{MAX_NUM};' * MAX_OPT_LEN)[:-3]], 
            f'{"3432393439363732393500" * MAX_OPT_LEN}'
        ],
    ]

    for case in cases:
        t.test(*case)

    t.done()    


if __name__ == "__main__":
    main()
