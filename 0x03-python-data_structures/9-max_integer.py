#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        m = my_list[0]
        for x in range(1, len(my_list)):
            if my_list[x] > m:
                m = my_list[x]
                return (m)
        return (m)
