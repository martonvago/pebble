#!/usr/bin/python

import ultraimport
ultraimport('__dir__/../tester.py', '*', locals())


# Given that a 4-digit (8-bit) hex number is on the working stack
# When print-decimal is called
# Then it prints the number in decimal
def main():
    t = Tester('print-decimal.test.tal')

    for hex_string in ['00000000', '00000001', '00000002', '0000abdf', 'ffffffff']:
        t.test(hex_string, [ushort_lit(hex_string)], str(int(hex_string, 16)))

if __name__ == "__main__":
    main()
