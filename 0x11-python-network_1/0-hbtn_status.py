#!/usr/bin/python3
# Python script that fetches https://intranet.hbtn.io/status
from urllib import request

req = request.Request("https://intranet.hbtn.io/status")

with request.urlopen(req) as response:
    body = response.msg
    content = response.peek()
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}".format(body))
