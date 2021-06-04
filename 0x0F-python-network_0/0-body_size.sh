#!/bin/bash
#takes in a url, sends a req to that url and displays the size of the body of the res.
curl -sI "$1" | grep 'Content-Length:' | cut -d' ' -f2
