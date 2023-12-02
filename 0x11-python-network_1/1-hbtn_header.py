#!/usr/bin/python3
'''Module that demonstrates how to work with the urlopen module of urlib'''
from urllib.request import urlopen
from urllib.error import URLError
import sys


def urlHeader():
    '''prints the value of 'x-request-id' in the received http header'''
    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} url")
    url = sys.argv[1]
    try:
        with urlopen(url) as response:
            header = response.headers
            print(header['X-Request-Id'])
    except (URLError, ValueError, TypeError) as msg:
        sys.exit(msg)


if __name__ == '__main__':
    urlHeader()
