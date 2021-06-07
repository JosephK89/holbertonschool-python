#!/usr/bin/python3
"""
takes in a url, sends a request to the url and displays the body of the response
"""
import requests
import sys

if __name__ == "__main__":
    r = request.get(sys.argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
