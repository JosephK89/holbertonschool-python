#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and
displays the body of the response"""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get(argv[1])
    status = r.status_code
    if status >= 400:
        print("Error code: " + str(status))
    else:
        print(r.text)
