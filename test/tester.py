#!/usr/bin/python

from subprocess import run, DEVNULL, call, Popen, PIPE, TimeoutExpired
import re, os, sys
from binascii import hexlify

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

NL = '\n'
MAX_NUM = (1 << 32) - 1
VOTES_LEN = 1024
MAX_COMMAND_NAME_LEN = 12
MAX_OPT_LEN = 1 << 8
INPUT_LEN = 2828
OPT = 3                 # hard coded until setup command impl

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

def blank_replace(_, inputs):
    return f"[ [ {inputs.pop(0)} ] ]"

def abs_path_to_file(file):
    here = os.path.dirname(os.path.abspath(file))
    tal_file = os.path.basename(file)[:-2] + 'tal'
    return os.path.join(here, tal_file)

class Tester:
    uxn_loc = '/home/marton/uxn/uxn/'
    uxnasm = uxn_loc + 'uxnasm'
    uxncli = uxn_loc + 'uxncli'
    placeholder = r'\[ \[.*?\] \]' 

    def __init__(self, file):
        self.filename = abs_path_to_file(file)
        self.rom = self.filename + '.rom'
        self.fail = False

    def interact(self, name, inputs, expected, wait=0.1):
        self._assemble()
        p = Popen([self.uxncli, self.rom], stdin=PIPE, stdout=PIPE)
        
        try:
            inputs = (NL.join(inputs) + NL).encode()
            p.stdout.flush() 
            got, errs = p.communicate(inputs, timeout=wait)
        except TimeoutExpired:
            p.stdout.flush() 
            p.kill()
            got, errs = p.communicate()

        p.kill()
        got = got.decode('utf-8').replace('>> ', '')
        self._check_results(name, got, expected)

    def test(self, name, inputs, expected):
        with open(self.filename, 'r+') as f:
            file = f.read()
            file = re.sub(self.placeholder, lambda matchobj: blank_replace(matchobj, inputs), file)

            f.seek(0)
            f.write(file)
            f.truncate()

        self._assemble()
        result = run([self.uxncli, self.rom], capture_output = True)
        
        got = result.stdout.decode('utf-8')
        self._check_results(name, got, expected)

    def done(self):
        sys.exit(self.fail)

    def _assemble(self):
        run([self.uxnasm, self.filename, self.rom], stderr = DEVNULL)

    def _check_results(self, name, got, expected):
        if got == expected:
            print(f"{Fore.GREEN}{name}: passed{Style.RESET_ALL}")
        else:
            self.fail = True
            case = {'got': got, 'expected': expected}
            print(f"{Fore.RED}{name}: failed{Style.RESET_ALL} ({case})")