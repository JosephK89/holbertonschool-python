#!/usr/bin/python3
"""
takes in a url and an email, sends a post request to the passed url with the
email as a parameter, and displays the body of the response
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    email = urllib.parse.urlencode({"email": sys.argv[2]})
    email = email.encode("ascii")
    with urllib.request.urlopen(sys.argv[1], email) as res:
        print(res.read().decode("utf-8"))
