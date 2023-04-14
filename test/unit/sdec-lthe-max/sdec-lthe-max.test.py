#!/usr/bin/python

import os, ultraimport
ultraimport('__dir__/../../tester.py', '*', locals())
ultraimport('__dir__/../test-utils.py', '*', locals())

# Given that a decimal string is saved in memory
# When sdec-lthe-max is called with the address of the first char of the string and the address of the string cap
# Then it returns True if the number is representable in 32 bits
def main():
    t = Tester(__file__)

    passes = ['0', '1', '2', '00', '01', '0094967295', '34967295', MAX_NUM, '0000000001', '0000000000']
    fails = ['42949672951', '00000000001', '00000000000', '4394967295', '5294967296', MAX_NUM + 1]

    for case in passes:
        t.test(case, [us(case)], ubyte(True)) 

    for case in fails:
        t.test(case, [us(case)], ubyte(False))  

    t.done()    


if __name__ == "__main__":
    main()
