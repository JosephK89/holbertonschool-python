#!/bin/bash
#takes in a url, sends a post req. to the passed url and displays the body of the res.
curl -X POST -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" -s "$1"
