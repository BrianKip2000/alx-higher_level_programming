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
        return self.width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError f'Width must be an integer'
        if width <= 0:
            raise ValueError f'Width must be >=0'
        self.width = width

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError f'height should be integer'
        if height <= 0:
            raise ValueError f'height must be >= 0'
        self.height = height

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x <= 0:
            raise ValueError("x must be >= 0")
        self.x = x

    @property
    def y(self):
        return self.y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an int")
        if y <= 0:
            raise ValueError("y must be >= 0")
        self.y = y
