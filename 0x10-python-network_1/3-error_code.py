#!/usr/bin/python3
"""
takes in a url, sends a request to the url and displays the body of the response
"""
import urllib.request
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            print(response.read().decode("utf-8"))
    except urllib.errror.HTTPError as e:
        error = str(e).split(" ")[2][:-1]
        print("Error code: {}".format(error))
