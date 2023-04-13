#!/usr/bin/python

import os, ultraimport
ultraimport('__dir__/../../tester.py', '*', locals())

# Given that a decimal string is saved in memory
# When sdec-to-hex is called with the address of the first char of the string
# Then it returns the number in 32-bit hex (8 hex digits)
def main():
    t = Tester(__file__)

    # <= ffff ffff
    cases = ['0', '00000000', '2', '00234', '4294967', MAX_NUM]
    for case in cases:
        t.test(case, [us(case)], hex8(int(case))) 
    
    # > ffff ffff
    t.test('overflow', [us(MAX_NUM + 1)], '00000000')        

    t.done()    


if __name__ == "__main__":
    main()
