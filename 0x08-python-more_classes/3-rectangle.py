#!/usr/bin/python3
"""
    Rectangle module

    """


class Rectangle:
    """
        Rectangle Class

        Attribute:
            width (int): Private
            height (int) : Private

        """
    def __init__(self, width=0, height=0):
        """
            Init Rectangle Class

        Args:
            width (int): The width of rectangle
            height (int): Thhe height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            width getter

            Return: The width of the Rectangle (int)
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Width setter
        Args:
            Value (int) : a value to set
        Raises:
            TypeError: When value is not int
            ValueError: When value is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            height getter

        Return: the height of the rectangle (int)
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            height setter
        Args:
            value (int) : value to be set
        Raises:
            TypeError: When value is not int
            ValueError: When value is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            Return Rectangle Area

        Return: (int) rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            Return the perimeter of rectangle

        Return : (int) rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return(self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
            print the rectangle

        Return:
            printed rectangle widh '#'
            """
        if self.__width == 0 or self.__height == 0:
            return ""
        return (('#'*self.__width + "\n")*self.__height)[:-1]
