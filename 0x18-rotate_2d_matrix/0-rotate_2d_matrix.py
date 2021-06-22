#!/usr/bin/python3
"""
rotate 2d matrix module
"""


def rotate_2d_matrix(matrix):
    """ rotate_2d_matrix function"""
    n = len(matrix[0])

    for i in range(n - 1, -1, -1):
        for x in range(0, n):
            matrix[x].append(matrix[i].pop(0))
