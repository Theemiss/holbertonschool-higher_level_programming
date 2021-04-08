#!/bin/bash
# send a get request with custome data and display body
curl -s "$1" -X GET -H 'X-HolbertonSchool-User-Id: 98' 
