#!/usr/bin/python3
"""
append after a specific string module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, "r+", encoding="utf-8") as f:
        s = ""
        for line in f:
            s += line
            if search_string in line:
                s += new_string
        f.seek(0)
        f.write(s)
