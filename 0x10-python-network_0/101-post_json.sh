#!/bin/bash
# Script that sends a requests to a URL argument, displays onyl the status code of the response
curl -s -X POST -H "Content-Type: application/json" -d @$2 $1
