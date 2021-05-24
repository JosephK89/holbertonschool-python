#!/usr/bin/python3
"""
mylist module
"""


class MyList(list):
    """mylistclass"""
    def print_sorted(self):
        """prints the list in ascending order"""
        print(sorted(self))
