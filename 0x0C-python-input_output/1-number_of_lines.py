#!/usr/bin/python3
"""
number of lines module
"""


def number_of_lines(filename=""):
    """number_of_lines fct"""
    with open(filename, encoding="utf-8") as file:
        return len(list(file))
