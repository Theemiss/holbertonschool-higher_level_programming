#!/usr/bin/python3
def uniq_add(my_list=[]):
    su = 0
    uniq = list(set(my_list))
    for x in uniq:
        su += x
    return (su)
