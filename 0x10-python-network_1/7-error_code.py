#!/usr/bin/python3
"""
takes in a url, sends a request to the URL and displays the body of the response
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get(argv[1])
    if r.status_code >= 400:
        print("Error code: {:s}".format(r.status_code))
    else:
        print(r.text)
