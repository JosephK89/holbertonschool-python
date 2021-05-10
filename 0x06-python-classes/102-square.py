#!/usr/bin/python3
"""define a class"""


class Square:
    """
    square class
    """
    def __init__(self, size=0):
        """initialization of the class
        """
        self.size = size

    def area(self):
        """area fct
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter fct
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter fct
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def __lt__(self, other):
        """1
        """
        return self.size < other.size

    def __le__(self, other):
        """2
        """
        return self.size <= other.size

    def __eq__(self, other):
        """3
        """
        return self.size == other.size

    def __ne__(self, other):
        """4
        """
        return self.size != other.size

    def __ge__(self, other):
        """5
        """
        return self.size >= other.size

    def __gt__(self, other):
        """6
        """
        return self.size > other.size
