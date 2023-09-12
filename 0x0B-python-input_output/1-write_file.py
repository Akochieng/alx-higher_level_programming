#!/usr/bin/python3
'''writes a string to a text file and returns the number of characters written'''


def write_file(filename="", text=""):
    '''functions that writes to a file

    Args:
        filename: the name of the file
        test: the tesxt to be written to the file
    Returns: the number of characters written
    '''
    with open(filename, "w", encoding="UTF-8") as f:
        num = f.write(text)
    print(f"{num}")
