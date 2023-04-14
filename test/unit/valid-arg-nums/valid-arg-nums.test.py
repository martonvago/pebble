#!/usr/bin/python

import os, ultraimport
ultraimport('__dir__/../../tester.py', '*', locals())
ultraimport('__dir__/../test-utils.py', '*', locals())

def arr(votes):
    chars = [to_ascii_code(n) for n in votes]
    body = '00'.join(chars)
    length = int(len(body) / 2)
    body = ' '.join(split_str_to_chunks(body, 2))
    return format(length, '04x'), body

# Given that the args of the add-results command are 
    # saved in memory and 
    # are well-formed and
    # have been parsed into an array (of decimal strings)
# When valid-arg-nums is called with the address of the first element, the array cap and the option number
# Then it returns True if 
    # all the numbers are representable in 32 bits and
    # the number of elements equals the number of options
def main():
    t = Tester(__file__)

    passes = [
        ['zero options', ['#00', '0000', '']],
        ['single option', ['#01', *arr([1])]],
        ['single option with unfilled array', ['#01', '0004', '34 00 00 00']],
        ['single option with 0 votes', ['#01', *arr([0])]],
        ['single option with max vote count', ['#01', *arr([MAX_NUM])]],
        ['multiple options', ['#03', *arr([1, 2, 3])]],
        ['higher vote counts', ['#03', *arr([2343, 0, 124234])]],
        ['vote counts with leading 0s', ['#03', *arr(['00000001', '002', '03'])]],
        ['max options', ['#ff', *arr([23] * 255)]],
        ['max options with max vote count for each', ['#ff', *arr([MAX_NUM] * 255)]],
    ]

    fails = [
        ['too many vote counts', ['#01', *arr([1, 2, 3])]],
        ['too few vote counts', ['#09', *arr([1, 2, 3])]],
        ['too few vote counts with unfilled array', ['#05', '0005', '34 00 00 00 00']],
        ['vote count too large', ['#03', *arr([1, MAX_NUM + 1, 3])]],
        ['max options with vote count too large for each', ['#ff', *arr([MAX_NUM + 1] * 255)]],
    ]

    for case in passes:
        t.test(*case, ubyte(True)) 

    for case in fails:
        t.test(*case, ubyte(False))

    t.done()    


if __name__ == "__main__":
    main()
