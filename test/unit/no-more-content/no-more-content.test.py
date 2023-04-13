#!/usr/bin/python

import os, ultraimport
ultraimport('__dir__/../../tester.py', '*', locals())

# Given that an array is saved in memory
# When no-more-content is called with a pointer into this array and the address of the array
# Then it returns True if all bytes from the pointer's target are 00
def main():
    t = Tester(__file__)

    no_more = [
        ['0-length array', ['#0000', '0000', '']],
        ['ptr to last element + 1', ['#0006', '0006', '11 22 33 44 55 66']],
        ['ptr to last element + 2', ['#0007', '0006', '11 22 33 44 55 66']],
        ['array empty from ptr', ['#0002', '0006', '11 22 00 00 00 00']],
        ['empty array, ptr at start', ['#0000', '0003', '00 00 00']],
        ['empty array, ptr at mid', ['#0001', '0003', '00 00 00']],
        ['empty array, ptr at end', ['#0002', '0003', '00 00 00']],
    ]

    more = [
        ['array full, ptr at start', ['#0000', '0006', '11 22 33 44 55 66']],
        ['array full, ptr at mid', ['#0002', '0006', '11 22 33 44 55 66']],
        ['array full, ptr at end', ['#0005', '0006', '11 22 33 44 55 66']],
        ['array empty later after ptr', ['#0002', '0006', '11 22 33 44 00 00']],
        ['array empty after ptr', ['#0002', '0006', '11 22 33 00 00 00']],
    ]
    
    for case in no_more:
        t.test(*case, ubyte(True))

    for case in more:
        t.test(*case, ubyte(False)) 

    t.done()    


if __name__ == "__main__":
    main()
