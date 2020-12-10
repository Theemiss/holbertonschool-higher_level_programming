#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def main(**argv):
    l = len(sys.argv)
    if l != 4:
        print('Usage: {} <a> <operator> <b>'.format(sys.argv[0]))
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == "+":
            print("{} {} {} = {}".format(a, sys.argv[2], b, add(a, b)))
        elif sys.argv[2] == "-":
            print("{} {} {} = {}".format(a, sys.argv[2], b, sub(a, b)))
        elif sys.argv[2] == "*":
            print("{} {} {} = {}".format(a, sys.argv[2], b, mul(a, b)))
        elif sys.argv[2] == "/":
            print("{} {} {}= {}".format(a, sys.argv[2], b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)


if __name__ == "__main__":
    main()
