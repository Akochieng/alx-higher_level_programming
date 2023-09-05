#!/usr/bin/python3
'''This module provides a function that is used to demonstrate
how to work with doc string in testing
'''


def matrix_divided(matrix, div):
    '''divides all elements of a matrix

    Args:
        matrix (list of lists): 2 by 2 matrix
        div (int): the divisor

    Returns: resulting lists of lists
    Raises:
        TypeError: if lists in the matrix are known of the same size
        TypeError: matrix must be a list of lists of intergers or floats
        TypeError: div must be a number
        ZeroDivisionError: division by zero
    '''
    if not (isinstance(div, float) or isinstance(div, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    el = len(matrix[0])
    for li in matrix:
        if not len(li) == el:
            raise TypeError("Each row of the matrix must have the same size")
    newlist = [list(map(lambda num: float(format(num / div, '.2f')), li)) for li in matrix]
    return newlist
