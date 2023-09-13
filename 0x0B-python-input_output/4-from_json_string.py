#!/usr/bin/python3
import json
'''demonstrates how to convert JSON strings to Python objects'''


def from_json_string(my_str):
    '''
    converts a JSON object to a python object

    Args:
        my_str: the JSON object

    Return: the decoded object
    '''
    the_dict = {}
    the_dict = json.loads(my_str)
    return the_dict
