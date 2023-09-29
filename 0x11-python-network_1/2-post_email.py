#!/usr/bin/python3
"""
a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import urllib.request as req
import urllib.parse as parse
from sys import argv


if __name__ == "__main__":
    val = {"email": argv[2]}
    add = parse.urlencode(val).encode("ascii")
    info = req.Request(argv[1], add)
    with req.urlopen(info) as response:
        print(response.read().decode("utf-8"))
