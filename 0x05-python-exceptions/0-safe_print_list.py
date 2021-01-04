#!/usr/bin/python3
"""
    prints x elements of a list.

    """


def safe_print_list(my_list=[], x=0):
    nb = 0
    for x in range(0, x):
        try:
            print(my_list[x], end="")
            nb += 1
        except:
            break
    print("")
    return(nb)
