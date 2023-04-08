#!/usr/bin/python

import sys, os, ultraimport
ultraimport('__dir__/../tester.py', '*', locals())

def dec_to_ubytelit(num):
    return ubyte_lit(ubyte(num))

# Given that two strings are saved in memory
# When seq-til is called with the absolute addresses of these strings and a limit (0 - ff)
# Then it returns a flag (0/1) whether the 2 strings are equal up to the limit
def main():
    t = Tester(__file__)

    for case in [
        ['when strings equal', 13, 'test string 1', 'test string 1', True],
        ['when strings equal and limit < len', 5, 'test string 1', 'test string 1', True],
        ['when strings equal and limit> len', 20, 'test string 1', 'test string 1', True],
        ['when strings equal and limit 0', 0, 'test string 1', 'test string 1', True],
        ['when strings not equal and limit 0', 0, 'abcd', 'test string 1', True],
        ['when strings not equal', 13, 'abcd', 'test string 1', False],
        ['when strings equal up to limit', 4, 'abcd', 'abcdtest string 1', True],
        ['when strings equal up to limit (spaces)', 4, '    ', '       ', True],
        ['when strings not equal (spaces)', 6, '    ', '       ', False],
        ['when limit max', 255, 'a', 'a', True],
    ]:
        t.test(case[0], [dec_to_ubytelit(case[1]), us(case[2]), us(case[3])], ubyte(case[4]))  

    sys.exit(t.fail)    


if __name__ == "__main__":
    main()
