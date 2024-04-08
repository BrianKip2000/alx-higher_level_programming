#!/usr/bin/python3
"""Class to define square dimensions"""


class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @property
    def size(self, value):
        """Raise errors if the values dont match criterion"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def area(self):
        return (self.__area * self.__area)

    @property
    def my_print(self):
        if size is not equal to 0:
            for square in range(0, self.size):
            print("#" * self.size)
        else:
            print(" ")
