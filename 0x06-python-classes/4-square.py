#!/usr/bin/python3
"""define a class"""


class Square:
    """squareclass"""
    
    def __init__(self, size=0):
        self.size = size

    def area(self):
        """area function"""
        return (self.__size)**2
    
    @property
    def size(self):
        """getter fct"""
        return self.__size
        
    @size.setter
    def size(self, val):
        """setter fct"""
        if type(val) is not int:
            raise TypeError("size must be an integer")
        if val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val
