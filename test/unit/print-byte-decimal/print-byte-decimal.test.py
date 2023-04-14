#!/usr/bin/python

import os, ultraimport
ultraimport('__dir__/../../tester.py', '*', locals())
ultraimport('__dir__/../test-utils.py', '*', locals())

# Given that a hex byte is on the working stack
# When print-decimal is called
# Then it prints the number in decimal without leading 0s
def main():
    t = Tester(__file__)

    for hex_string in ['00', '01', '02', '10', 'df', 'ff']:
        t.test(hex_string, [hex_string], str(int(hex_string, 16)))

    t.done()    

if __name__ == "__main__":
    main()
