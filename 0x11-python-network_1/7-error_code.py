#!/usr/bin/python3
import requests
import sys
"""
same as 3-error_code with requests model
"""

if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
