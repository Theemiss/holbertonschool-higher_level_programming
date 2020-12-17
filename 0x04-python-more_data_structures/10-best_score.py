#!/usr/bin/python3
def best_score(a_dictionary):
    m = 0
    b = ''
    if a_dictionary is None:
        return None
    for i in a_dictionary.keys():
        if a_dictionary[i] > m:
            m = a_dictionary[i]
            b = i
    return b
