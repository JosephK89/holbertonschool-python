#!/usr/bin/python3
"""
takes in a url, sends a request to the url and displays the body of the response
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get(argv[1])
<<<<<<< HEAD
    status = r.status_code
    if status >= 400:
        print("Error code: " + str(status))
=======
    if r.status_code >= 400:
        print("Error code: {:s}".format(r.status_code))
>>>>>>> a6b47f1db61fd5e7d53340df583d781b4b191b1d
    else:
        print(r.text)
