#!/usr/bin/python3
import sys


def main(*argv):
    x = 0
    lth = len(sys.argv)
    if lth == 2:
        print("{:d} argument:".format(lth-1))
    elif lth == 1:
        print("{:d} argument.".format(lth-1))
    else:
        print("{:d} arguments:".format(lth-1))
    for args in sys.argv:
        if (x != 0):
            print("{}: {}".format(x, args))
        x += 1
if __name__ == "__main__":
    main()
