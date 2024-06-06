#!/usr/bin/python3

def add_integer(a, b=98):
    """add_integer is a funtion two add two integers
    if both are integers, a result is generated
    if not an error is raised
    arguments:
        a: int or float
        b: int equal to 98
    """
    if not isinstance(a, (int, float)):
        raise ValueError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise ValueError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
