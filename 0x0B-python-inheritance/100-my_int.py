#!/usr/bin/python3
"""
myint module
"""


class MyInt(int):
    """MyInt class"""
    def __eq__(self, other):
        """eq"""
        return super().__ne__(other)

    def __ne__(self, other):
        """ne"""
        return super().__eq__(other)
