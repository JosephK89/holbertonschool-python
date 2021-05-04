#!/usr/bin/python3
def roman_to_int(roman_string):
    values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    if type(roman_string) is not str or roman_string is None:
        return 0
    ans = 0
    for i in range(len(roman_string)):
        if i > 0 and values[roman_string[i]] > values[roman_string[i - 1]]:
            ans += values[roman_string[i]] - 2 * values[roman_string[i - 1]]
        else:
            ans += values[roman_string[i]]
    return ans
