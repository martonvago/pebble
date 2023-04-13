#!/usr/bin/python

import os, ultraimport
ultraimport('__dir__/../../tester.py', '*', locals())

# Given that there is a long on the WS
# When sta4 is called with the long and an address in memory pointing to a long
# Then it saves the long to the given address
def main():
    t = Tester(__file__)
    addr1 = ';addr1'
    addr2 = ';addr2'

    cases = ['abcdef12', '00000000', '00000001', '10000000', '00001000', 'ffffffff', '0012345a', '23000000']

    for case in cases:
        t.test(f'{case} to first addr', [ushort_lit(case), addr1], case + '00000000')  
        t.test(f'{case} to second addr', [ushort_lit(case), addr2], '00000000' + case)  

    t.done()    


if __name__ == "__main__":
    main()
