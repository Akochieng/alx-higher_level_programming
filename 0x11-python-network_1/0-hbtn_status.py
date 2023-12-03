#!/usr/bin/python3
'''This module describes how to work with urllib's request module'''
from urllib.request import urlopen
from urllib import error as err


def fetchURL():
    '''Function that prints the type of content received from a url'''
    try:
        with urlopen("https://alx-intranet.hbtn.io/status") as response:
            body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")
    except err as msg:
        print(msg)


if __name__ == '__main__':
    fetchURL()
