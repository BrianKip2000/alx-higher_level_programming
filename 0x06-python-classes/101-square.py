#!/usr/bin/python3
"""Print Square Instance"""


class Square:
    """Class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialization of function:
        args:
            size(int): size of square is an int
            position(int, optional): position of square at every instance."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Return size as a protected instance.
        It is a getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Function to set value of size
         args:
            value(int): value should be an int
        raise:
            TypeError: if value is not an integer
            ValueError: if size is less than 0"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Property setter:
                Returns:
                    self.__position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Function definition:
            args:
                value(tuple): value should be a tuple
            raise:
                TypeError: 'position must be a tuple of two integers'"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integer")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        if not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integer")
        if not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Return area of the square."""
        return self.size * self.size

    def my_print(self):
        """Public instance function to print output"""
        if self.size == 0:
            print()
            return
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
