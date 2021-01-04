#!/usr/bin/python3
import sys
"""
     function that prints an integer
    """


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return False
