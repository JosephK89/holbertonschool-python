#!/usr/bin/python3
"""
search and update module
"""


def append_after(filename="", search_string="", new_string=""):
    """append_after fct"""
    with open(filename, "r") as file:
        text = file.readlines()

    with open(filename, "w") as file:
        s = ""
        for line in text:
            s += line
            if search_string in line:
                s += new_string
        file.write(s)
