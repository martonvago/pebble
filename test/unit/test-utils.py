#!/usr/bin/python

import re
from binascii import hexlify

def hex8(num):
    return '{0:08x}'.format(num)

def to_ascii_code(string):
    return hexlify(str(string).encode()).decode()

def ubyte_lit(string):
    string = ubyte(string)
    return re.sub(r'..', lambda matchobj: f"#{matchobj.group(0)} ", string)[:-1]

def ushort_lit(string):
    return re.sub(r'....', lambda matchobj: f"#{matchobj.group(0)} ", string)[:-1]

def ubyte(num):
    return format(num, '02x')

def ushort(num):
    return format(num, '04x')

def split_str_to_chunks(string, size):
    result = []
    while len(string) > 0:
        result.append(string[:size])   
        string = string[size:]
    return result

def _split_str_to_max_chunks(string):
    return split_str_to_chunks(string, 60)            

def _uword(matchobj):
    string = matchobj.group(0)
    if string.isspace():
        return ' 20 '
    chunks = _split_str_to_max_chunks(string)
    return '"' + ' "'.join(chunks)


def us(string):
    return re.sub(r'(\S+)|(\s)', _uword, str(string)) + ' $1'