#!/usr/bin/python3
'''Module that demonstrates how to work with urlopen module'''
from urllib.request import urlopen
from urllib.error import URLError
from urllib.error import HTTPError
from urllib.parse import urlencode
import sys


def urlHeader():
    '''prints the decoded value of the received urlopen response'''
    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} url")
    url = sys.argv[1]
    try:
        with urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except HTTPError as msg:
        errm = msg
        print(f"Error code: {errm.getcode()}")
    except (URLError, ValueError, TypeError) as msg:
        sys.exit(msg)


if __name__ == '__main__':
    urlHeader()
