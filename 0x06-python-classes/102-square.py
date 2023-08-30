#!/usr/bin/python3
'''
This module uses class square to demonstrate how to work with classes
in Python3 effectively
'''


class Square:
    '''
    This is a simple class with two major attributes: size and position
    '''

    def __init__(self, size=0):
        '''
        This init function has two major attributes size and position.

        Args:
            size (float): must always be >= 0
        '''
        self.__size = size

    @property
    def size(self):
        '''
        Args:
            new_size (float): must be an int greater than or equal to 0

        Return:
            The new size

        Raises:
            TypeError: if the value is not of type int
            ValueError: If the value is not greater than 0
        '''
        return self.__size

    @size.setter
    def size(self, new_size):
        if not isinstance(new_size, float):
            raise TypeError("size must be a number")
        elif new_size < 0:
            raise ValueError("message size must be >= 0")
        else:
            self.__size = new_size

    def area(self):
        '''
        Simple method that returns the current square area

        Return: Area of the square
        '''
        return self.__size * self.__size

    def __str__(self):
        '''
        Simple method that returns the string formated with position

        Return: The string representation of square adjusted for position
        '''
        sq_str = ""
        if self.__size > 0:
            for i in range(1, self.__size + 1):
                sq_str += "#" * self.__size
                if i < self.__size:
                    sq_str += "\n"
        else:
            sq_str += "\n"
        return sq_str

    def my_print(self):
        '''
        simple method that prints the square using #
        it relies on the str method above
        '''
        print(self.__str__())

    def __eq__(self, other):
        '''
        Tests whether self is equal to the other

        Args:
            other: the other object of type square
        Return:
            True or False
        '''
        if isinstance(other, Square):
            if self.__size == other.__size:
                return True
        return False

    def __ne__(self, other):
        '''
        Tests whether self is not equal to the other

        Args:
            other: the other object
        Return:
            True or False
        '''
        return (not self.__eq__(other))

    def __lt__(self, other):
        '''
        Tests whether self is less than the other

        Args:
            other: the other object
        Return:
            True or False
        '''
        return self.__size < other.size

    def __gt__(self, other):
        '''
        Tests whether self is greater than the other

        Args:
            other: the other object
        Return:
            True or False
        '''
        return self.__size > other.size

    def __le__(self, other):
        '''
        Tests whether self is less than or equal to the other

        Args:
            other: the other object
        Return:
            True or False
        '''
        return self.__size <= other.size

    def __ge__(self, other):
        '''
        Tests whether self is greater than or equal to the other

        Args:
            other: the other object
        Return:
            True or False
        '''
        return self.__size >= other.size
