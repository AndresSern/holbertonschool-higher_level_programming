#!/usr/bin/python3
"""
Script that takes in a URL and email, sends a POST request to the passed URL
the email as a parameter, and displays the body of the response(decoded in
utf-98)
"""
from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    values = {'email': argv[2]}
    data = parse.urlencode(values)
    data = data.encode("ascii")
    req = request.Request(argv[1], data)
    with request.urlopen(req) as respons:
        print(respons.read().decode("utf-8"))
