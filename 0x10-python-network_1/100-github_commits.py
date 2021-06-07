#!/usr/bin/python3
"""
lists 10 commits
"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get("https://api.github.com/repos/{}/{}/commits".format(sys.argv[2], sys.argv[1]))
    if r.status_code >= 400:
        print("None")
    else:
        for x in r.json()[:10]:
            print("{}: {}".format(x.get("sha"),com.get("commit").get("author").get("name")))
