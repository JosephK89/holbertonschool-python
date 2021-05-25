#!/usr/bin/python3
"""
pascal's triangle module
"""


def pascal_triangle(n):
    """pascal_triangle fct"""
    l = [[] for i in range(n)]
    for i in range(n):
        for j in range(i+1):
            if j < i:
                if j == 0:
                    l[i].append(1)
                else:
                    l[i].append(l[i-1][j]+l[i-1][j-1])
            elif j == i:
                l[i].append(1)
    return l
