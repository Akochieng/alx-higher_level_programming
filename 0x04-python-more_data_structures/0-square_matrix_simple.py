#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmat = [list(map(lambda x: x * x, mat)) for mat in matrix]
    return (newmat)
