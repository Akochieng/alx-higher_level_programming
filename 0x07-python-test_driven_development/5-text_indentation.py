#!/usr/bin/python3
'''simple module that transforms strings'''
def text_indentation(text):
    '''adds 2 new lines after every . , ? or :

    Args:
        text (str): must be a string
    Returns:
        None
    Raises:
        TypeError: if text is not a string
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    transdict = {".": ".\n\n", ",": ",\n\n", "?": "?\n\n", ":": ":\n\n"}
    table = str.maketrans(transdict)
    print(text.translate(table), end="")
