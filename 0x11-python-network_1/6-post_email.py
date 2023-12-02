#!/usr/bin/python3
'''Demonstrates how to work with the request module'''
import requests
from requests import exceptions
from sys import argv
import sys


def displayVal():
    '''Prints the received body text'''
    if len(argv) != 3:
        sys.exit(f"Usage: {argv[0]} url email")
    url = argv[1]
    payload = {'email': argv[2]}
    try:
        with requests.post(url, data=payload) as response:
            res = response.text
            print(f"{res}")
    except exceptions as msg:
        sys.exit(msg)


if __name__ == '__main__':
    displayVal()
