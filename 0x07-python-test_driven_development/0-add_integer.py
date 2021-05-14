#!/usr/bin/python3
"""
    add integer module
    contains add_integer fct
    that return sum of two int
"""


def add_integer(a, b=98):
    """
    returns the sum of the two int
    """
    
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
        
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
        
    return a + b
