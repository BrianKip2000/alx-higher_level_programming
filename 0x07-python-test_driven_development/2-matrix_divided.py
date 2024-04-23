#!/usr/bin/python3

def matrix_divided(matrix, div):
    """Matrix funtion definition:
        matrix_divided - funtion for the diviion purpose
        @matrix: matrix input
        @div : division argument
        TODO:
        checks if the matrix is a float or an integer.
        if not, it should raise a TypeError with message:
        "matrix must be amatrix of int or float"
        also, if matrix length of row and column are not the same size:
        raise another TypeError with different exception message.
        if division is not by float or integer: raise another TypeError
        lastly, if division is by zero, raise ZeroDivisionError"""
    if not all(isinstance(row, list)
               and all(isinstance(item, (int, float))
                       for item in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
