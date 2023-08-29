#!/usr/bin/python3
'''Square Module
This module demonstrates how to work with classes.

The functionality included in this module is only for
demonstration purposes.
'''


class Square:
    '''Class square describes a square with size size'''
    def __init__(self, size=0):
        '''The class square implements a typical square

        The following parameters are initialised when the class
        is first initialised.

        Args:
            size (float): the length or width of the square
            '''
        self.set_size(size)

    def set_size(self, size):
        '''The set_size method defines the __size private attribute.
        It basically takes in size as a parameter and assigns it to
        the parameter __size.

        Args:
            size (int):The size parameter

        Returns:
            Nothing at all. Just sets the __size attribute

        Raises:
            TypeError: If parameter is not an interger
            ValueError: If parameter is not greater than 0
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an interger")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
