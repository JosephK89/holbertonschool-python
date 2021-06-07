#!/usr/bin/python3
"""
takes in a url and an email address, sends a post request to the passed url with the email as a parameter, and finally displays the body of the response
"""
import requests
import sys

if __name__ == "__main__":

    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
