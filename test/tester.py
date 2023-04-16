#!/usr/bin/python

from subprocess import run, DEVNULL, call, Popen, PIPE, TimeoutExpired, STDOUT
import re, os, sys
import ultraimport

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

ultraimport('__dir__/constants.py', '*', locals())
colorama_init()

uxnasm = 'uxnasm'       # path to uxnasm (if not on path)
uxncli = 'uxncli'       # path to uxncli (if not on path)
check = '\U00002705'
cross = '\U0000274C'

def blank_replace(_, inputs):
    return f"[ [ {inputs.pop(0)} ] ]"

def abs_path_to_file(file):
    here = os.path.dirname(os.path.abspath(file))
    tal_file = os.path.basename(file)[:-2] + 'tal'
    return os.path.join(here, tal_file)

class Tester:
    placeholder = r'\[ \[.*?\] \]' 

    def __init__(self, file):
        self.filename = abs_path_to_file(file)
        self.rom = self.filename + '.rom'
        self.sym = self.rom + '.sym'
        self.fail = False

    def interact(self, name, inputs, expected, wait=0.1, ignore_filler=True):
        self._assemble()
        p = Popen([uxncli, self.rom], stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        
        try:
            inputs = (NL.join(inputs) + NL).encode() if inputs else ''
            p.stdout.flush() 
            got, errs = p.communicate(inputs, timeout=wait)
        except TimeoutExpired:
            p.stdout.flush() 
            p.kill()
            got, errs = p.communicate()

        p.kill()
        got = got.decode('utf-8')
        if ignore_filler:
            got = got.replace('>> ', '').replace(welcome, '')
        self._check_results(name, got, expected)

    def test(self, name, inputs, expected):
        with open(self.filename, 'r+') as f:
            file = f.read()
            file = re.sub(self.placeholder, lambda matchobj: blank_replace(matchobj, inputs), file)

            f.seek(0)
            f.write(file)
            f.truncate()

        self._assemble()
        result = run([uxncli, self.rom], stdout=PIPE, stderr=STDOUT)
        
        got = result.stdout.decode('utf-8')
        self._check_results(name, got, expected)

    def done(self):
        sys.exit(self.fail)

    def _assemble(self):
        if os.path.exists(self.rom): os.remove(self.rom)
        if os.path.exists(self.sym): os.remove(self.sym)
        run([uxnasm, self.filename, self.rom], stderr = DEVNULL)

    def _check_results(self, name, got, expected):
        if got == expected:
            print(f" {check} {Fore.GREEN}{name}{Style.RESET_ALL}")
        else:
            self.fail = True
            case = {'got': got, 'expected': expected}
            print(f" {cross} {Fore.RED}{name}{Style.RESET_ALL}\n({case})")