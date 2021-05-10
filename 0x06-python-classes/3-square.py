#!/usr/bin/python3
"""define a class"""


class Square:
    """squareclass"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """area function"""
        a = (self.__size) ** 2
        return a
