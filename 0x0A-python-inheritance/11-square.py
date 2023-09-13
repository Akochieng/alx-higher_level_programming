#!/usr/bin/python3
'''simple module to demonstrate inheritance'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Rectangle with equal height and width'''
    def __init__(self, size):
        '''initialises the super class attributes'''
        super().__init__(size, size)

    def __str__(self):
        '''returns string representation of the class'''
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
