#!/usr/bin/python3
"""
a Python script that takes in a URL,
sends a request to the URL
displays the body of the response (decoded in utf-8).
"""
import requests
from sys import argv


if __name__ == "__main__":
    info = requests.get(argv[1])
    if info:
        print(info.text)
    else:
        print("Error code: {}".format(info.status_code))
