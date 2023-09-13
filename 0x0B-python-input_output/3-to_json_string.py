#!/usr/bin/python3
import json
'''module that demonstrates how to work with JSON'''


def to_json_string(my_obj):
    '''returns the JSON representation of an object string

    Args:
        my_obj: the string object
    Return: the JSON representation
    '''
    return (json.dumps(my_obj))
