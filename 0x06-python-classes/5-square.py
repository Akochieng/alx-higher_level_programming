#!/usr/bin/python3
'''Square Module
This module demonstrates how to work with classes.

The functionality included in this module is only for
demonstration purposes.
'''


class Square:
    '''class Square
    This is a simple class to demonstrate how to work with properties
    setters, and getters. It also demonstrates how to work with private
    and public attributes
    '''
    def __init__(self, size=0):
        '''The class square implements a typical square

        The following parameters are initialised when the class
        is first initialised.

        Args:
            size (float): the length or width of the square
            '''
        self.__size = size

    @property
    def size(self):
        '''The getter functions returns the value of the size attribute

        The setter method has the following characteristics

        Args:
            newsize: the size of the square

        Returns:
            does not return anythong

        Raises:
            TypeError: if size is not of type interger
            ValueError: If size is not >= 0
        '''
        return self.__size
    @size.setter
    def size(self, newsize):
        if not isinstance(newsize, int):
            raise TypeError("size must be an interger")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = newsize

    def area(self):
        '''The area method calculates the area of the square
        the parameter __size.

        Args:
            no arguments.

        Returns:
            The area of the square

        Raises:
            No exception. Expected to be always successful
        '''
        return self.__size * self.__size

    def my_print(self):
        '''Draws a square using #

        Args:
            no arguments.

        Returns:
            Nothing

        Raises:
            No exception. Expected to be always successful
        '''
        times = 0
        if self.__size == 0:
            print("")
        else:
            c = "#" * self.__size
            while times < self.__size:
                print(f"{c}")
                times += 1
