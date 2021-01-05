#!/usr/bin/python3
""" Module Sqaure """


class Square:
    """ Square class defined by geometric shap

        Attributes:
            size (int): Size of square
    """
    def __init__(self, size=0):
        """
        Initialize methode

        Args:
            size (int): int to assign to square size
        Raises:
            TypeError: if size is not int
            ValueError: size less than 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
