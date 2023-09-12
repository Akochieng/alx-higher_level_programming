#!/usr/bin/python3
'''simple module to demonstrate how to work with open'''


def read_file(filename=""):
    '''opens a file to read the text and print to the standard
    output

    Args:
        filename: the name of the file

    Return: None
    '''
    with open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            print(line, end="")
