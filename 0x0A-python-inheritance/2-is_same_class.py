#!/usr/bin/python3
'''helps with checking if the object is an instance of a class'''


def is_same_class(obj, a_class):
    '''checks whether obj is an instance of the a_class

    Args:
        obj: the object
        a_class: the class

    Returns: True or False
    '''
    return isinstance(obj, a_class)
