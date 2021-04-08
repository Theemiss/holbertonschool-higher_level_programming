#!/bin/bash
# send a post request with custome data
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
