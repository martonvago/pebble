#!/usr/bin/python

from subprocess import run, DEVNULL, call
import re, os

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

def ubyte_lit(string):
    return re.sub(r'..', lambda matchobj: f"#{matchobj.group(0)} ", string)[:-1]

def ushort_lit(string):
    return re.sub(r'....', lambda matchobj: f"#{matchobj.group(0)} ", string)[:-1]

def us(string):
    string = re.sub(r'\S+', lambda matchobj: f"\"{matchobj.group(0)}", string)
    return re.sub(' ', ' 20 ', string) + ' $1'

def ubyte(num):
    return format(num, '02x')

def blank_replace(_, inputs):
    return f"[ [ {inputs.pop(0)} ] ]"

def abs_path_to_file(filename, location):
    here = os.path.dirname(os.path.abspath(location))
    return os.path.join(here, filename)

class Tester:
    uxn_loc = '/home/marton/uxn/uxn/'
    uxnasm = uxn_loc + 'uxnasm'
    uxncli = uxn_loc + 'uxncli'
    placeholder = r'\[ \[.*\] \]' 

    def __init__(self, filename, f):
        self.filename = abs_path_to_file(filename, f)
        self.rom = filename + '.rom'
        self.fail = False

    def test(self, name, inputs, expected):
        with open(self.filename, 'r+') as f:
            file = f.read()
            file = re.sub(self.placeholder, lambda matchobj: blank_replace(matchobj, inputs), file)

            f.seek(0)
            f.write(file)
            f.truncate()

        run([self.uxnasm, self.filename, self.rom], stderr = DEVNULL)
        result = run([self.uxncli, self.rom], capture_output = True)
        
        got = result.stdout.decode('utf-8')

        if got == expected:
            print(f"{Fore.GREEN}{name}: passed{Style.RESET_ALL}")
        else:
            self.fail = True
            case = {'got': got, 'expected': expected}
            print(f"{Fore.RED}{name}: failed{Style.RESET_ALL} ({case})")

