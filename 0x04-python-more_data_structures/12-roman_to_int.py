#!/usr/bin/python3
def roman_to_int(roman_string):
    if len(roman_string) == 0 or not isinstance(roman_string, str):
        return 0
    n = 0
    rom_to_int = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
    for i in roman_string:
        for j in rom_to_int.keys():
            if j == i:
                n += rom_to_int[j]
    return(n)
