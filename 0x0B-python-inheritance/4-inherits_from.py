#!/usr/bin/python3
"""
inherts from module
"""


def inherits_from(obj, a_class):
    """inherits_from fct"""
    return isinstance(obj, a_class) and type(obj) != a_class
