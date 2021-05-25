#!/usr/bin/python3
"""
write to a file module
"""


def write_file(filename="", text=""):
    """write file fct"""
    with open(filename, mode = "w", encoding = "utf-8") as file:
        return file.write(text)
