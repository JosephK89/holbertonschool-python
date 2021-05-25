#!/usr/bin/python3
"""
read file module
"""


def read_file(filename=""):
    """read_file fct"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
