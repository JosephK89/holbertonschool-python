#!/usr/bin/python3
"""
takes in a url and an email, sends a post request to the passed url with the
email as a parameter, and displays the body of the response
"""
import requests
import sys

if __name__ == "__main__":
    r = request.post(sys.argv[1], data={"email": sys.argv[2]})
    print(r.text)
