#!/usr/bin/python3
"""
takes in a url and an email address, sends a post request to the passed url with the email as a parameter, and finally display the body of the response
"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.post(argv[1], data={"email": argv[2]})
    print(r.text)
