#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
"""
import requests
from sys import argv

if __name__ == "__main__":
    res = requests.get("https://intranet.hbtn.io/status")
    body = res.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
