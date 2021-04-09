#!/usr/bin/python3
"""
Script that takes in a URL and an email address, sends a POST request to the
passed URL with the email as a paramater , and finally diplays the body of the
response
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    data = {"email": argv[2]}
    res = requests.post(argv[1], data=data)
    print(res.text)
