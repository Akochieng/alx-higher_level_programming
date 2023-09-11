#!/usr/bin/python3
'''checks if an instance of a class that inherited directly or indirectly from
the specified class'''


def inherits_from(obj, a_class):
    '''checks whether obj is a direct or indirect instance of a_class

    Args:
        obj: the object
        a_class: the class
    Returns: True or False
    '''
    return isinstance(obj, a_class)
