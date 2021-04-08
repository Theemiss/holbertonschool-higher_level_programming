#!/bin/bash
#get statue code from http header  work just task(curl -sI "$1" | grep "HTTP/" |  cut -d " " -f 2)
curl -so /dev/null --write-out "%{http_code}" "$1"
