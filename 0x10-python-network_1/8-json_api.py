#!/usr/bin/python3
"""
takes in a letter and sends a post request to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        dic = r.json()
        if dic == {}:
            print("No result")
        else:
            print("[{}] {}".format(dic.get("id"), dic.get("name"))
    except:
        print("Not a valid JSON")
