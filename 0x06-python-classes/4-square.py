#!/usr/bin/python3
"""Square Class"""


class Square:
    """Initialize the size attribute"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @property
    def size(self, value):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size * self.__size)
