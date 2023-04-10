#!/usr/bin/python

import sys, os, ultraimport
ultraimport('__dir__/../tester.py', '*', locals())

# Given that there is a long saved in memory 
# When lda4 is called with the address of the long
# Then it returns the long
def main():
    t = Tester(__file__)

    cases = ['abcd ef12', '0000 0000', '0000 0001', '1000 0000', '0000 1000', 'ffff ffff', '0012 345a', '2300 0000']

    for case in cases:
        t.test(case, [case], case.replace(' ', ''))  

    sys.exit(t.fail)    


if __name__ == "__main__":
    main()
