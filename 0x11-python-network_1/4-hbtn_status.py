#!/usr/bin/python3
'''Demonstrates how to work with the request module'''
import requests
from requests import exceptions


def fetchURL():
    '''prints the type and content of a response'''
    url = 'https://alx-intranet.hbtn.io/status'
    try:
        with requests.get(url) as response:
            res = response.text
            print("Body response:")
            print(f"\t- type: {type(res)}")
            print(f"\t- content: {res}")
    except exceptions as msg:
        print(msg)


if __name__ == '__main__':
    fetchURL()
