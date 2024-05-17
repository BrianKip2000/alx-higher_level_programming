#!/usr/bin/python3
"""Class to inherit from Baseclass"""
from models.base import Base


class Rectangle(Base):
    """Child class of Base."""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Width setter"""
        return self.__width

    @width.setter
    def width(self, width):
        """Checks if width is of type int and greater than 0:"""
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be >=0')
        self.__width = width

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """Height setter checking for type int and >= 0 situation"""
        if type(height) is not int:
            raise TypeError('height should be integer')
        if height <= 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    @property
    def x(self):
        """Returns size of x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets x if its int and greater than 0"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x <= 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter if its int and greater than 0"""
        if not isinstance(y, int):
            raise TypeError("y must be an int")
        if y <= 0:
            raise ValueError("y must be >= 0")
        self.__y = y
