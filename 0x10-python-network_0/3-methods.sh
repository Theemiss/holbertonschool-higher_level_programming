#!/bin/bash
# display allowed http method 
curl -sI "$1" -X OPTIONS | grep "Allow" | cut -c 8-
