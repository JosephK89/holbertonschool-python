#!/bin/bash
#takes in a url as an arg., sends a get req. to the url and displays the body of the res.
curl -H "X-HolbertonSchool-User-Id: 98" -s "$1"
