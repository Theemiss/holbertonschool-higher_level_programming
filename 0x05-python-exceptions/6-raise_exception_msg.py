#!/usr/bin/python3
"""
    function that raises a type exception with message
    """


def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except:
        raise
