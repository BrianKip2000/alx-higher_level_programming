#!/usr/bin/python3
"""Module to check for Geometry"""


class BaseGeometry:
    """
    Defines the base geometry class.
    """

    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            Exception: Indicates that the method is not implemented.
        """
        raise Exception("area() is not implemented")
