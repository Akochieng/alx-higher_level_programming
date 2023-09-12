#!/usr/bin/python3
'''function that appends a string to a file'''
def append_write(filename="", text=""):
    '''appends a string at the end of a text file

    Args:
        filename: file to be opened
        text: the text to be appended
    Returns:
        The number of characters written
    '''
    with open(filename, "a", encoding="utf-8") as f:
        num = f.write(text)
    return num
