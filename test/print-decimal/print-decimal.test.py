#!/usr/bin/python
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

from math import floor, log
from os import environ
from random import randint
from subprocess import Popen, PIPE, run

colorama_init()

uxn_loc = '/home/marton/uxn/uxn/'
uxnasm = uxn_loc + 'uxnasm'
uxncli = uxn_loc + 'uxncli'

u1  = {'sz': 1, 'fmt': b'%02x'}
u3  = {'sz': 1 << 3,  'fmt': b'%02x'} 
u5  = {'sz': 1 << 5,  'fmt': b'%02x'}
u8  = {'sz': 1 << 8,  'fmt': b'%02x'}
u16 = {'sz': 1 << 16, 'fmt': b'%04x'} 
u32 = {'sz': 1 << 32, 'fmt': b'%08x'} # format to at least 8 hex digits

# Given that a 4-digit (8-bit) hex number is saved in memory
# When print-decimal is called
# Then it prints the number in decimal
def testcase(p, hex_string): 

    # i want to write a number in hex
    # to change base and fix format: '{0:08x}'.format(num)
    # but this is string
    # stdin accepts bytes (?) so i turn my hex number into b'hexnumber'
    # bytes object: sequence of numbers 0-255 (= 0-ff)
    #       --> can be printed conveniently as ascii chars
    #       <-- can be created from ascii chars

    # i have a hex string
    expected = str(int(hex_string, 16))         # number in decimal
    byte_object = bytes.fromhex(hex_string)     # turn this into a byte object
    p.stdin.write(byte_object)                  # now it can be sent
    p.stdin.write(b'\n')                        # submit (by sending byte-object for newline)
    p.stdin.flush()

    got = p.stdout.readline().strip().decode('utf-8')

    if got == expected:
        return None
    else:
        res = {'got': got, 'expected': expected}
        return res

def test(p, hex_string):
    success = False
    maximum = (1 << 32) - 1
    case = testcase(p, hex_string)
    if case is None:
        success = True
    name = hex_string
    if success:
        print(f"{Fore.GREEN}{name} passed{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}{name} failed{Style.RESET_ALL} ({case})")

def pipe():
    return Popen([uxncli, 'run.rom'], stdin=PIPE, stdout=PIPE)

def main():
    run([uxnasm, 'print-decimal.test.tal', 'run.rom'])
    p = pipe()

    test(p, '00000000')
    test(p, '00000001')
    test(p, '00000002')
    test(p, '0000abdf')
    test(p, 'ffffffff')
    
    p.stdin.close()
    p.stdout.close()
    p.kill()

if __name__ == "__main__":
    main()
