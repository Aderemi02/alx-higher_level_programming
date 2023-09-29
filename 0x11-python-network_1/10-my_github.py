#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":
    user = HTTPBasicAuth(argv[1], argv[2])
    info = requests.get("https://api.github.com/user", auth=user)
    profile = info.json()
    print(profile.get("id"))
