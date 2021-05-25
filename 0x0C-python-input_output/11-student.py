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
    
    def to_json(self):
        """to_json fct"""
        return self.__dict__
