#!/bin/bash
#get statue code from http header 
curl -sI "$1" | grep "HTTP/" |  cut -d " " -f 2
