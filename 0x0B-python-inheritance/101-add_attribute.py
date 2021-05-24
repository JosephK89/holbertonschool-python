#!/usr/bin/python3
"""
add attribute module
"""


def add_attribute(obj, atr, value):
    """add_attribute fct"""
    if not hasattr(obj, "__slots__") and not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    if hasattr(obj, "__slots__") and not hasattr(obj, atr):
        raise TypeError("can't add new attribute")
    setattr(obj, atr, value)
