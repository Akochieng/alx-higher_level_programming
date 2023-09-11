#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
'''simple module to demonstrate inheritance'''


class Square(Rectangle):
    '''Rectangle with equal height and width'''
    def __init__(self, size):
        '''initialises the super class attributes'''
        super().__init__(size, size)
