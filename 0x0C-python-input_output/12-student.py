#!/usr/bin/python3
"""
student to json module
"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """initialization of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json fct"""
        mydict = dict()
        if type(attrs) is list and all(type(x) is str for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    mydict.update({x: self.__dict__[x]})
            return mydict
        return self.__dict__
