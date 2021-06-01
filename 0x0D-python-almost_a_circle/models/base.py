#!/usr/bin/python3
"""
base module
"""


class Base:
    """base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """initialization of the class"""
        if id is not None:
            self.id = id
        Base.__nb_object += 1
