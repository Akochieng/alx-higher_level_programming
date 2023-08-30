#!/usr/bin/python3
'''Square Module
This module demonstrates how to work with classes.

The functionality included in this module is only for
demonstration purposes.
'''


class Square:
    '''The class square implements a typical square

    The following parameters are initialised when the class
    is first initialised.

    Args:
        size (float): the length or width of the square
        '''
    def __init__(self, size):
        '''This is the init function for the square class
            Currently, it takes not parameters
            '''
        self.__size = size
