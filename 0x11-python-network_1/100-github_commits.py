#!/usr/bin/python3
"""
That takes your GITHUB credentials(username and password) and uses the
GitHub Api to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    repository = argv[1]
    name = argv[2]
    repository_name = "{}/{}/commits".format(name, repository)
    res = requests.get("https://api.github.com/repos/" + repository_name)
    commit_json = res.json()
    for i, commit_current in enumerate(commit_json):
        if i == 10:
            break
        idCommit = commit_current["sha"]
        nameCommit = commit_current["commit"]["author"]["name"]
        print("{}: {}".format(idCommit, nameCommit))
