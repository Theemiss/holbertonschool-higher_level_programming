#!/usr/bin/python3
import urllib.request
import sys
"""
sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response
"""

if __name__ == '__main__':
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        info = response.read()
    print(info.decode("ascii"))
