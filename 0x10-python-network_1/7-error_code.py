#!/usr/bin/python3
"""
takes in a url, sends a request to the url and displays the body of the response
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get(argv[1])
    status = r.status_code
    if status >= 400:
        print("Error code: " + str(status))
    else:
        print(r.text)
