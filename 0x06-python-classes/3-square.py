#!/usr/bin/python3
""" Module Sqaure """


class Square:
    """ Square class defined by geometric shap

        Attributes:
            size (int): Size of square
    """
    def __init__(self, size=0):
        """
        initializes the square
        Args:
            size (int): size of a side of the square
        Raises:
            TypeError: if size is not int
            ValueError: size less than 0
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
                raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
            set square square area

            Return:
                the current square area (int)
        """
        return self.__size ** 2
