#!/bin/bash
curl -sI $1 | grep -oP '(?<=Allow: ).*'
