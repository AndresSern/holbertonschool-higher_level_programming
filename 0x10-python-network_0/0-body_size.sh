#!/bin/bash
# Takes in a URL sends a request to that URL and displays the size of the body
curl -so /dev/null $1 -w '%{size_download}\n'
