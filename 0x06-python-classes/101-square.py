#!/usr/bin/python3
"""define a class"""


class Square:
    """square class
    """
    def __init__(self, size=0, position=(0, 0)):
        """initializes the square
        """
        self.size = size
        self.position = position

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
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("".join([" " for k in range(self.__position[0])]), end="")
            print("".join(["#" for l in range(self.__size)]))

    @property
    def position(self):
        """getter fct
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setterfct
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def __str__(self):
        """str
        """
        if self.size == 0:
            return ""
        string = "\n" * self.position[1] + (" " * self.position[0] +
                                            "#" * self.size + "\n") * self.size
        return string[:-1]
