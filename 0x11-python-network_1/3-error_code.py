#!/usr/bin/python3
"""
request a body if error display statue code
"""

if __name__ == '__main__':
    import urllib.request
    import urllib.error
    import sys
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            info = response.read()
            print(info.decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
