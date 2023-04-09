#!/usr/bin/python

import sys, os, ultraimport
ultraimport('__dir__/../tester.py', '*', locals())

def expected(string):
    chunks = string.split(';') 
    if '' in chunks: chunks.remove('')
    chunks = [ to_ascii_code(c) for c in chunks ]
    return '00'.join(chunks)

# Given that the args of the add-results command are saved in memory and are well-formed
# When prep-arg is called with the address of the first char
# Then it replaces the semicolons with 00 terminators
def main():
    t = Tester(__file__)

    for case in ['0', '0;', '00', '00;', '2', '2;', '1;2;3;', '1;2;3', '33;44;55;66', '00023;12321;0;12;1232', 
        f'{MAX_NUM};', f'{MAX_NUM + 1};', f'{MAX_NUM};{MAX_NUM}', f'{MAX_NUM};' * 9 ]:
        t.test(case, [us(case)], expected(case)) 

    sys.exit(t.fail)    


if __name__ == "__main__":
    main()
