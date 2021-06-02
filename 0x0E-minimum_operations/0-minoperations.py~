#!/usr/bin/python3
"""
minimum operations module
"""


def minOperations(n):
    """minOperations function"""
    if n <= 1:
        return 0
    result = 0
    div = 2
    while n > 1:
        if n % div == 0:
            n /= div
            result += div
        else:
            div += 1
    return result
