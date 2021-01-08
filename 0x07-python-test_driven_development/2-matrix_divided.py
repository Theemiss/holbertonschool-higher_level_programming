#!/usr/bin/python3
"""
Module Devide Matrix
    """


def matrix_divided(matrix, div):
    """
        Devides all elements in matrix

        Args:
            matrix (list[list[int/float]]) : matrice
            div (int/float) Devider

        Raise:
            TypeError: div not int or float
            TypeError: matix is not a list of list of number
            ZeroDivisionError: Div is 0

        Return : New matrix Devided

        """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(matrix) is not list or not all((type(l) is list)for l in matrix) \
        or not all((isinstance(n, (int, float))for n in l)for l in matrix) \
            or len(matrix[0]) == 0:
        raise TypeError(
                "matrix must be a matrix "
                "(list of lists) of integers/floats")
    l = len(matrix[0])
    if not all((len(x) == l)for x in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return [list(map(lambda x: round(x / div, 2), r))for r in matrix]
