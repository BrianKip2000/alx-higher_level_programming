#!/usr/bin/python3
from models.rectangle import Rectangle
"""module for creating a square based on rect"""


class Square(Rectangle):
    """Class that takes its properties from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes Square class instance:
        Args:
            size (int): size of the square equal to rect dim
            x (any): positional argument
            y (any): positional argument
            id : unique id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the class"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")
