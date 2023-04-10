#!/usr/bin/python

import sys, os, ultraimport
ultraimport('__dir__/../tester.py', '*', locals())

# Given that a long is on the WS
# When lthe-ff is called
# Then it returns True if the number is <= ff
def main():
    t = Tester(__file__)

    passes = ['00000000', '00000001', '0000001a', '000000ff']
    fails = ['ffffffff', '00000100', '0000011a', '67780000']

    for case in passes:
        t.test(case, [ushort_lit(case)], ubyte(True)) 

    for case in fails:
        t.test(case, [ushort_lit(case)], ubyte(False))  

    sys.exit(t.fail)    


if __name__ == "__main__":
    main()
