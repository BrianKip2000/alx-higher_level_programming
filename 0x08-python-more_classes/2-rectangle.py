#!/usr/bin/python3
"""Class to find the area and perimeter and area of rectangle"""


class Rectangle:
    """Rectangle class that takes height and width as its variables"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Module to return width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Module to check for height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Module to multiply width an height to get area"""
        return self.width * self.height

    def perimeter(self):
        """Module to add the total distance covered in the rectangle"""
        if (self.height == 0 or self.width == 0):
            return 0
        else:
            return 2 * (self.width + self.height)
