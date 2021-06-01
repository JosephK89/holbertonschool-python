#!/usr/bin/python3
"""
rectangle module
"""

base = __import__('base.py').base


class Rectangle(base):
    """rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization of the class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @width.setter
    def width(self, value):
        """width setter"""
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""
        self.__height = value

    @x.setter
    def x(self, value):
        """x setter"""
        self.__x = value

    @y.setter
    def y(self, value):
        """y setter"""
        self.__y = value
