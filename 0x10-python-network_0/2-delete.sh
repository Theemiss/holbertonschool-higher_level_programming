#!/bin/bash
# send a delete request over to the url introduced as argument
curl -s "$1" -X DELETE
