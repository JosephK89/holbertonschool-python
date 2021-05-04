#!/usr/bin/python3
def roman_to_int(roman_string):
    values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    if type(roman_string) is not str or roman_string is None:
        return 0
    ans = 0
    for i in range(len(roman_string)-1,-1,-1):
        num = values[roman_string[i]]
        if 4 * num < ans:
            ans -= num
        else: 
            ans += num
    return ans
