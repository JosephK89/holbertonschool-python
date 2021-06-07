#!/usr/bin/python3
"""
takes in a url, sends a request to the url and displays the body of the response
"""
import urllib.request
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            print(res.read().decode("utf-8"))
    except HTTPError as ex:
        print("Error code: {}".format(e.code))
