#!/usr/bin/python3
"""
square module
"""

BaseGeometry = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size):
        """initalization of the class"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
        
    def area(self):
        """returns the area of the square"""
        return self.__size ** 2
    
    def __str__(self):
        """returns string representation of the square"""
        return "[Square] {:d}/{:d}".format(self.__width, self.__height)
