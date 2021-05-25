#!/usr/bin/python3
"""
append write module
"""


def append_write(filename="", text=""):
    """append_write fct"""
    with open(filename, mode="a", encoding="utf-8") as file:
        characters = file.write(text)
    return characters
