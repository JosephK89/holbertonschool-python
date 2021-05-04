#!/usr/bin/python3
def roman_to_int(roman_string):
    values = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    if type(roman_string) is not str or roman_string is None:
        return 0
    sum=0
    while i < len(roman_string) - 1
        a = values[roman_string[i]]
        b = values[roman_string[i + 1]]
        if a == b:
            sum += a + b
            i += 1
        elif a < b:
            sum += b - a
            i += 1
        else:
            sum += a
        i += 1
    return sum
