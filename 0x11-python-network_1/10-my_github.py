#!/usr/bin/python3
"""
That takes your GITHUB credentials(username and password) and uses the
GitHub Api to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    headers = {"Authorization": 'token'}
    res = requests.get("https://api.github.com/user",
                       auth=HTTPBasicAuth(username, password))
    id_json =res.json().get("id")
    print(id_json)
