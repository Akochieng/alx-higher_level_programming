#!/usr/bin/python3
'''Square Module
This module demonstrates how to work with classes.

The functionality included in this module is only for
demonstration purposes.
'''


class Square:
    '''class Square is a simple class to demonstrate how to
    work with classes and objects
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''The class square implements a typical square

        The following parameters are initialised when the class
        is first initialised.

        Args:
            size (float): the length or width of the square
            position (tuple): a tuple with intergers on both values
            to represent the position of the square
            '''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''
        The size getter function returns the current size of the object

        The setter function sets the new value and its called everytime
        the size attribute needs to be updated

        Args:
            newsize: the new size of the attribute. It must be an interger

        Returns:
            None

        Raises:
            TypeError: If the attribute is not of type interger
            ValueError: If the value is less than 0
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
    @property
    def position(self):
        '''
        Position describes the position of the square in the stdout.
        The getter function only returns the value of self.__position

        The setter value sets the new value of the position attribute

        Args:
            value: the new value of position

        Return:
            None

        Raises:
            TypeError: the value must be a tuple of 2 intergers
        '''
        return self.__position
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not (isinstance(value[0], int) and isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
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
            c = " " * self.__position[0] + "#" * self.__size
            print("{}".format("\n" * self.__position[1]),end='')
            while times < self.__size:
                print(f"{c}")
                times += 1
