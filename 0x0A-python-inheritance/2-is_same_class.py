#!/usr/bin/python3
"""
    is_same_class
"""


def is_same_class(obj, a_class):
    """
    check instance and class
    Args:
        obj(object):to be checked
        a_class(anything): to be checked
    Return: True or False
    """
    return type(obj) is a_class
