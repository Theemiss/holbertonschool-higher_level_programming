#!/usr/bin/python3
"""
A Student class that defines a Studen (module)
"""


class Student():
    """
        A Student class that defines a Student
    """
    def __init__(self, first_name, last_name, age):
        """
            INIT
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            retrieves a dictionary representation
            of a Student instance
        """
        return(self.__dict__)
