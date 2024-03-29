#!/usr/bin/python3
"""
a Python script that takes in a URL,
sends a request to the URL and displays the value of the X-Request-Id
variable found in the header of the response.
"""
import requests
from sys import argv


if __name__ == "__main__":
    loc = requests.get(argv[1])
    print(dict(loc.headers).get("X-Request-Id"))
