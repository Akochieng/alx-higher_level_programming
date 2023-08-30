#!/usr/bin/python3
'''
This module uses class square to demonstrate how to work with classes
in Python3 effectively
'''


class Square:
    '''
    This is a simple class with two major attributes: size and position
    '''

    def __init__(self, size=0, position=(0, 0)):
        '''
        This init function has two major attributes size and position.

        Args:
            size (int): must always be >= 0
            position (tuple): must be a tuple of intergers
        '''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''
        Args:
            new_size (int): must be an int greater than or equal to 0

        Return:
            The new size

        Raises:
            TypeError: if the value is not of type int
            ValueError: If the value is not greater than 0
        '''
        return self.__size

    @size.setter
    def size(self, new_size):
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("message size must be >= 0")
        else:
            self.__size = new_size

    @property
    def position(self):
        '''
        Args:
            value (tuple): must be a tuple of integers

        Return: The new value of __position

        Raises:
            TypeError: if the value is not a tuple of integers
        '''
        return self.__position

    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple) and len(value) == 2):
            raise TypeError("position must be a tuple of 2 positive integer")
        elif not (isinstance(value[0], int) and isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integer")
        else:
            self.__position = value

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
        height_offset = self.__position[1] * "\n"
        width_offset = self.__position[0] * " "
        sq_str += height_offset
        if self.__size > 0:
            for i in range(1, self.__size + 1):
                sq_str += width_offset + ("#" * self.__size)
                if i < self.__size:
                    sq_str += "\n"
            return sq_str
        else:
            print("")

    def my_print(self):
        '''
        simple method that prints the square using #
        it relies on the str method above
        '''
        print(self.__str__())
