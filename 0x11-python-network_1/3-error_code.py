#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the body
of the response(decoded in UTF-8)
"""
from urllib import request, parse, error
from sys import argv

if __name__ == "__main__":
    res = request.Request(argv[1])
    try:
        with request.urlopen(res) as respons:
            print(respons.read().decode("utf-8"))
    except error.URLError as exception:
        print("Error code: {}".format(exception.code))
