#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that takes its properties from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the class"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")
    
