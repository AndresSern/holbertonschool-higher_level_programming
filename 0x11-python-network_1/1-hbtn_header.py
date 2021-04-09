#!/usr/bin/python3
"""
Script that takes in a url, sends a request and show the value of the
X-Request-Id variable found in the header of the reponse h
"""
from urllib import request
from sys import argv

if __name__ == "__main__":

    req = request.Request(argv[1])
    with request.urlopen(req) as response:
        print(response.headers["X-Request-Id"])
