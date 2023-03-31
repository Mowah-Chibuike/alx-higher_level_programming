#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sL "$(curl -sL --head "$1" | grep -q 200 && echo "$1")"
