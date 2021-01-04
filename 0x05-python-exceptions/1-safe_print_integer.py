#!/usr/bin/python3
"""
    prints an integer with "{:d}".format().

    """


def safe_print_integer(value):
    try:
        print('{:d}'.format(value))
        return(True)
    except:
        return False
