#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nmatrix = []
    for i in matrix:
        arr = []
        for j in i:
            arr.append(j * j)
        nmatrix.append(arr)
    return nmatrix
