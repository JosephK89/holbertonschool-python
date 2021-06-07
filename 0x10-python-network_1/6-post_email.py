#!/usr/bin/python3
"""
takes in a url and an email address, sends a post request to the passed url
with the email as a parameter, and finally displays the body of the response
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.post(argv[1], data={"email": argv[2]})
    print(r.text)
