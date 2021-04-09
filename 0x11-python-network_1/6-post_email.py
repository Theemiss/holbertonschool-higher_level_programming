#!/usr/bin/python3
import requests
import sys
"""
same as 2-post_email with requests models
"""

if __name__ == '__main__':
    para = {"email": sys.argv[2]}
    r = requests.post(sys.argv[1], data=para)
    print(r.text)
