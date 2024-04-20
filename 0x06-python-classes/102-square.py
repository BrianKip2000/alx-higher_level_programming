#!/usr/bin/python3
"""Comparing 2 squares"""


class Square:
    """Class Initialization"""
    def __init__(self, size=0):
        """__init__ function containing two param:
        @size: size variable"""
        self.__size = size

    @property
    def size(self):
        """Property getter containing size as the output:
        return: returns private attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size contains as an integer:
        raises TypeError if number is not a float or int"""
        if not isinstance(value, float):
            raise TypeError("size must be a number")
        if not isinstance(value, int):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area as a public attribute:
        return: public attribute self.area"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()
