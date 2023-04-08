#!/usr/bin/python

import sys, os, ultraimport
ultraimport('__dir__/../tester.py', '*', locals())

# Given that the args of the add-results command are saved in memory 
    # i.e. a string containing semicolon-separated list of decimal numbers
# When prep-arg is called with the address of the first char of the string
# Then it returns True if the string is well-formed
    # not empty
    # contains only digits or semicolon
    # starts with digit
    # ends with semicolon or digit
    # no two consecutive semicolons
def main():
    t = Tester(__file__)
    passes = ['0', '0;', '00', '00;', '2', '2;', '1;2;3;', '1;2;3', '33;44;55;66', '00023;12321;0;12;1232', 
        f'{MAX_NUM};', f'{MAX_NUM + 1};', f'{MAX_NUM};{MAX_NUM}', f'{MAX_NUM};' * 9 ]
    fails = ['a', ';0', ';;', '1;;', '1;;2', '1;2;w;3', '']

    for case in passes:
        t.test(case, [us(case)], ubyte(True)) 

    for case in fails:
        t.test(case, [us(case)], ubyte(False))  

    sys.exit(t.fail)    


if __name__ == "__main__":
    main()
