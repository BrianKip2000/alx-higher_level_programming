#!/usr/bin/python3

"""Module print_square
Printing square size"""


def print_square(size):
    """Funtion module to print size of square using #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if (size is float and size < 0):
        raise TypeError("size msut be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
