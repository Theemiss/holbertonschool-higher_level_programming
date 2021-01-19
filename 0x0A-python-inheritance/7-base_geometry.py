#!/usr/bin/python3
"""
    BaseGeometry module
"""


class BaseGeometry():
    """
        BaseGeometry Class
    """
    def area(self):
        """
            public instance
            Raise:
                Exception: Area not implemented

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Public instance  that validates value
            Args:
                name (string): name
                value(int): Value
            Raises:
                TypeError: When Value is not int
                ValueError: When Value less or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
