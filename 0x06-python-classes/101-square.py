#!/usr/bin/python3
"""
Square module.
"""


class Square:
    """
    Square define a geometric shape square
    Attributes:
        size (int): the size of the square
        position (tuple): the square position
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Init method is a constructor fo Square class
        Args:
            size (int): the size of the square
            position (tuple): a tuple of integer represent
                the position of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter of the size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter of the size attribute
        Args:
            value (int): an integer assigned to to the square size
        Raises:
            TypeError: if size not an integer
            ValueError: if size less than 0
        """
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter of the position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter of the position attribute
        Args:
            value (tuple): a tuple of integer represent
                the position of the square
        Raises:
            TypeError: if position not tuple and had not 2 positive integer
        """
        if not type(value) is tuple or len(value) != 2 \
                or not type(value[0]) is int or not type(value[1]) is int \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Area returns the current square area
        Returns:
            integer: the square area
        """
        return self.__size**2

    def my_print(self):
        """
        Prints the square forming by '#' symbol
        """
        if self.__size == 0:
            print()
        else:
        
            print('\n'*self.__position[1], end='')
            for i in range(0, self.__size):
                print(' '*self.__position[0], end='')
                print('#'*self.__size)

    def __str__(self):
        string = ""
        if self.__size == 0:
            return "\n"

        string += '\n'*self.__position[1]
        for i in range(self.__size):
            string += ' '*self.__position[0]
            string += '#'*self.__size
            if i is not self.__size - 1:
                string += '\n'
        return string