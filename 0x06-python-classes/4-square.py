#!/usr/bin/python3
'''Square Module
This module demonstrates how to work with classes.

The functionality included in this module is only for
demonstration purposes.
'''


class Square:
        '''The class square implements a typical square

        it does not have any class attributes. All instance
        attributes are defined in the init function below.
            '''
    def __init__(self, size=0):
        '''
        Args:
            size (float): the length or width of the square
            '''
        self.__size = size

    @property
    def size(self):
        '''size: the length of the square
        The property has a setter and getter method.
        The setter method has the following attributes:

        Args:
            size (int): the length of the square

        Returns:
            Does not return anythin. It only sets the __size attribute

        Raises:
            TypeError: If size is not of type int
            ValueError: If the size is not >= 0
        '''
        return self.__size
    @size.setter
    def size(self, newsize):
            TypeError: If parameter is not an interger
            ValueError: If parameter is not greater than 0
        if not isinstance(newsize, int):
            raise TypeError("size must be an integer")
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
