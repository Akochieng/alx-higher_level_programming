#!/usr/bin/python3
'''Simple module to demonstrate how to work with doc strings'''
def say_my_name(first_name, last_name=""):
    '''simple function to print the first and last name

    Args:
        first_name (str): the first name
        last_name (str): the last name
    Returns:
        None
    Raises:
        TypeError: if first_name is not a string
        TypeError: if last_name is not a string
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
