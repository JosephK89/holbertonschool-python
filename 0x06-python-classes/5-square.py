#!/usr/bin/python3
"""define a class"""


class Square:
    """square class
    """
    def __init__(self, size=0):
        """initializes the square
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

    def my_print(self):
        """print fct
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
