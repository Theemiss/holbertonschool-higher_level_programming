#!/usr/bin/python3
"""
    prints the first x elements of a list and only integers.

    """


def safe_print_list_integers(my_list=[], x=0):
    nb = 0
    for y in range(0, x):
        try:
            print("{:d}".format(my_list[y]), end="")
            nb += 1
        except(TypeError, ValueError):
            pass
    print()
    return(nb)
