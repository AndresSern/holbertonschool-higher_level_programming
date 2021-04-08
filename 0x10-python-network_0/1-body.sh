#!/bin/bash
# takes in a URL sends a GET request to URL and displays the body the response
curl -so /dev/null $1 -w '%{size_download}\n'
