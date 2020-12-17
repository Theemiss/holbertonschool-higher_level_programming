#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = list(my_list)
    for x in range(0, len(new) - 1):
        if new[x] == search:
            new[x] = replace
    return (new)
