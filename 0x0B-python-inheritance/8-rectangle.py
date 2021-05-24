#!/usr/bin/python3
"""
rectangle module
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class"""
    def __init__(self, width, height):
        """initalization of the class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
