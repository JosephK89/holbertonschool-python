#!/bin/bash
#sends a delete req. to the url passed as the first arg. and display the body of the res.
curl -X "DELETE" -s "$1"
