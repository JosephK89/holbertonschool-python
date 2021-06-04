#!/bin/bash
#sends a req to a url passed as an arg., and displays only the status code of the res.
curl -sI -w '%{response_code}' "$1" -o /dev/null
