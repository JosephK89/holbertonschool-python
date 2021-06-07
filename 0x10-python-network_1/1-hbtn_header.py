#!/usr/bin/python3
"""
takes in a url, sends a request to the url and displays the value of the
X-Request-Id variable found in the header of the response
"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        head = res.headers.get("X-Request-Id")
        print(head)
