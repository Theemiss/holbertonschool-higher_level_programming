#!/usr/bin/python3
"""
    Square Printer Module
    """


def print_square(size):
    """
        Print square using #
    Args:
        size (int) : Size of Square

    Raise
        TypeError: if size is not int
        ValueError: if size is less than 0
        TypeError: if size is float and less than 0
    Return:
        Printed Square
        """

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        print("#" * size)
