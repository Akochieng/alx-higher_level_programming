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
