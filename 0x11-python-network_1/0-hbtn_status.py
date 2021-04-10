#!/usr/bin/python3
"""
fetch holberton /statue page
"""

if __name__ == '__main__':
    import urllib.request
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        html = response.read()

    print("Body response:")
    print("\t- type: {}".format(html.__class__))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('ascii')))
