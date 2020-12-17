#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    m = 0
    for k, v in a_dictionary.items():
        if v > m:
            res = k
            m = v
    return res
