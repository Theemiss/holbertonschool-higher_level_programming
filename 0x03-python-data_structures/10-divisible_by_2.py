#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = list(my_list)
    for x in range(0, len(my_list)):
        if x % 2 is 0:
            new[x] = True
        else:
            new[x] = False
    return new
