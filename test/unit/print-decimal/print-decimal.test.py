#!/usr/bin/python

import os, ultraimport
ultraimport('__dir__/../../tester.py', '*', locals())


# Given that a hex long is on the working stack
# When print-decimal is called
# Then it prints the number in decimal without leading 0s
def main():
    t = Tester(__file__)

    for hex_string in ['00000000', '00000001', '00000002', '10000000', '00001000', '0000abdf', 'ffffffff']:
        t.test(hex_string, [ushort_lit(hex_string)], str(int(hex_string, 16)))

    t.done()    

if __name__ == "__main__":
    main()
