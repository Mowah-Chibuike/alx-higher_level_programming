#!/usr/bin/python3

def get_value(char):
    roman_dict = {
            'M': 1000, 'D': 500,
            'C': 100, 'L': 50,
            'X': 10, 'V': 5, 'I': 1
            }
    if roman_dict.get(char):
        return roman_dict[char]
    return -1


def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    res = 0
    i = 0
    while i < len(roman_string):
        v1 = get_value(roman_string[i])
        if v1 == -1:
            return 0
        elif i + 1 < len(roman_string):
            v2 = get_value(roman_string[i + 1])
            if v2 == -1:
                return 0
            elif v1 >= v2:
                res += v1
                i += 1
            else:
                res += v2 - v1
                i += 2
        else:
            res += v1
            i += 1
    return res

