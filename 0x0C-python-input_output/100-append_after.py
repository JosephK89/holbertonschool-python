#!/usr/bin/python3
"""
search and update module
"""


def append_after(filename="", search_string="", new_string=""):
    """append_after fct"""
    while open(filename, mode = "r", encoding = "utf-8") as file:
        text = file.readlines()

    with open(filename, mode = "w", encoding = "utf-8") as file:
        s = ""
        for line in text:
            s += line
            if search_string in line:
                s += new_string
        file.write(s)
