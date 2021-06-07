#!/usr/bin/python3
"""
takes in a url, send a request to the url and displays the body of the response
"""
import urllib.request
import sys

if __name__=="__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            print(res.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
