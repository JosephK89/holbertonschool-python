#!/bin/bash
#sends a json post req. to a url passed as the first arg., and displays the body of the res.
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2" 
