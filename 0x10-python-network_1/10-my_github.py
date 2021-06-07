#!/usr/bin/python3
"""
takes in github credentials (username and password) and uses the github api
to display an id
"""
import requests
import sys

if __name__ == "__main__":
    r = request.get("https://api.github.com/user", auth=(sys.argv[1], sys.argv[2]))
    if r.status_code >= 400:
        print("None")
    else:
        print(r.json().get("id"))
