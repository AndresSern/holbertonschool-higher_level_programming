#!/bin/bash
# Script that sends a requests to a URL argument, displays onyl the status code of the response
curl -s -o /dev/null -w "%{http_code}" $1
