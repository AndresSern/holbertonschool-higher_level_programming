#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the url and displays the body
of the response
"""
import requests
from sys import argv

if __name__ == "__main__":
    try:
        res = requests.get(argv[1])
        res.raise_for_status()
        print(res.text)
    except requests.exceptions.HTTPError as error:
        status_code = error.response.status_code
        print("Error code: {}".format(status_code))
