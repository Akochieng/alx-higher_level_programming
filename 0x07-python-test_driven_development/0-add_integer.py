#!/usr/bin/python3
'''
This module demonstrates how to work with doc strings
in testing
'''


def add_integer(a, b=98):
    '''add_interger

    Args:
        a (int or float): value to be added
        b (int or float): value to be added

    Returns:
        a float or an integer

    Raises:
        TypeError: <val> must be an interger
    '''
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
