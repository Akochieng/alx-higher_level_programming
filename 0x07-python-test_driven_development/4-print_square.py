#!/usr/bin/python3
'''
This is a simple module that demonstrates how to work with python doctests
'''


def print_square(size):
    '''prints a square using #

    Args:
        size (int): must be an integer
    Return:
        None
    Raises:
        TypeError: if size is a float and less than 0
        TypeError: If size is not an integer
        ValueError: if size is an integer but less than 0
    '''
    if isinstance(size, float):
        if size < 0:
            raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for times in range (size):
        print("{}".format("#" * size))
