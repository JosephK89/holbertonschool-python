#!/usr/bin/python3
"""
mylist module
"""


class Mylist(list):
    """mylist class"""
    def print_sorted(self):
        """prints the list in ascending order"""
        print(sorted(self))
