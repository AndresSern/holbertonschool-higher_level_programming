#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to
http://0.0.0.:5000/search_user with the letter as a  parameter
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) == 1:
        print("No result")
        quit()
    letter = argv[1]
    res = requests.post(url, data={"q": letter})
    try:
        res_json = res.json()
    except:
        print("Not a valid JSON")
    else:
        if len(res_json) == 0:
            print("No result")
        else:
            print("[{}] {}".format(res_json["id"], res_json["name"]))
