#!/usr/bin/python3
"""
read n lines module
"""


def read_lines(filename="", nb_lines=0):
    """read_lines fct"""
    with open(filename, encoding="utf-8") as file:
        if nb_lines <= 0:
            print(file.read(), end="")
        for i in range(nb_lines):
            line = file.readline()
            print(line, end="")
