#!/usr/bin/python3
"""
a Python script that takes in a URL,
sends a request to the URL
displays the body of the response (decoded in utf-8).
"""
import urllib.request as req
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    try:
        with req.urlopen(argv[1]) as response:
            print(response.read().decode("ascii"))
    except HTTPError as error:
        print("Error code: {}".format(error.code))
