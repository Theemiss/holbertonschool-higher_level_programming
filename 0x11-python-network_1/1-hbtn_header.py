#!/usr/bin/python3
import urllib.request
import sys
"""
fetch X-Request-Id from header response with url
introduced as argument
"""

if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        content = response.getheader('X-Request-Id')

    print(content)
