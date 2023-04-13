#!/usr/bin/python

import ultraimport
ultraimport('__dir__/../tester.py', '*', locals())

def main():
    t = Tester(__file__)

    t.interact('name', ['start vote', 'vote 1'], 'Vote cast\n')

    t.done()    


if __name__ == "__main__":
    main()
