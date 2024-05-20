#!/usr/bin/python3
"""module for creating a square based on rect"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that takes its properties from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes Square class instance:
        Args:
            size (int): size of the square equal to rect dim
            x (any): positional argument
            y (any): positional argument
            id : unique id(str)
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the class"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """Getter for width form size"""
        return self.width

    @size.setter
    def size(self, value):
        """Method for setting the class size
        shall be equal to width and height"""
        if type(value) is not int:
            raise TypeError(f"width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns attributes"""
        attributes = ['id', 'size', 'x', 'y']

        for index, value in enumerate(args):
            if index < len(attributes):
                setattr(self, attributes[index], value)
        for key, value in kwargs.items():
            if key in attributes:
                setattr(self, key, value)
