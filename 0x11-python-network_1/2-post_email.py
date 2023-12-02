#!/usr/bin/python3
'''Module that describes how to work with the urlopen module'''
from urllib.request import urlopen
from urllib.error import URLError
from urllib.parse import urlencode
import sys


def urlHeader():
    '''puts an email to the received url'''
    if len(sys.argv) != 3:
        sys.exit(f"Usage: {sys.argv[0]} url email")
    url = sys.argv[1]
    params = {'email': f'{sys.argv[2]}'}
    encoded = urlencode(params).encode()
    try:
        with urlopen(url, data=encoded) as response:
            body = response.read()
            print(body.decode())
    except (URLError, ValueError, TypeError) as msg:
        sys.exit(msg)


if __name__ == '__main__':
    urlHeader()
