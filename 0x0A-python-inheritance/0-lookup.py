#!/usr/bin/python3
"""
module of the lookup function
"""


def lookup(obj):
    """returns a list of available attributes and methods of an object"""
    return dir(obj)
