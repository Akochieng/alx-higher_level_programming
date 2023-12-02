#!/usr/bin/python3
'''Demonstrates how to work with the request module'''
import requests
from requests import exceptions
from requests.exceptions import HTTPError
from sys import argv
import sys


def displayVal():
    '''Prints the received body text or failure code'''
    if len(argv) != 2:
        sys.exit(f"Usage: {argv[0]} url")
    url = argv[1]
    try:
        with requests.get(url) as response:
            res = response.text
            response.raise_for_status()
            print(f"{res}")
    except HTTPError as msg:
        print(f"Error code: {msg.response.status_code}")
    except exceptions as msg:
        print(msg)


if __name__ == '__main__':
    displayVal()
