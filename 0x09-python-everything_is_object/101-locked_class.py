#!/usr/bin/python3
'''Simple modulc to demonstrate the concept of locked classes'''


class LockedClass:
    '''This is an empty class that prevents a user from creating
    dynamic attributes'''
    __slots__ = ['first_name']

    def __init__(self):
        first_name = ""
