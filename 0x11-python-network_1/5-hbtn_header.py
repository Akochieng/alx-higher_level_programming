#!/usr/bin/python3
'''Demonstrates how to work with the request module'''
import requests
from requests import exceptions
from sys import argv
import sys


def displayVal():
    '''prints the value of the X-Request-Id header'''
    if len(argv) != 2:
        sys.exit(f"Usage: {argv[0]} url")
    url = argv[1]
    try:
        with requests.get(url) as response:
            header = response.headers
            print(f"{header['X-Request-Id']}")
    except KeyError as msg:
        sys.exit(msg)
    except exceptions as msg:
        sys.exit(msg)


if __name__ == '__main__':
    displayVal()
