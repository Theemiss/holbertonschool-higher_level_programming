#!/usr/bin/python3
def best_score(a_dictionary):
    m = 0
    res = ""
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v > m:
                res = k
                m = v
        return res
    else:
        return None
