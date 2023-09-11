#!/usr/bin/python3
'''Empty class'''


class BaseGeometry:
    '''simple class to demonstrate how to work with classes'''
    def __init__(self):
        '''
        No parameters or attributes to be initialised
        '''
        pass

    def area(self):
        '''sample method. Not really implemented

        Raises: Exception - area() is not implemented
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''checks whether value is an interger and greater than 0

        name: a string
        value: the value

        Raises:
            TypeError: if not an integer
            ValueError: value is greater than 0
        '''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
