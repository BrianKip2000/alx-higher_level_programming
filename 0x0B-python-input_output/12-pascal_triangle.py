#!/usr/bin/python3
"""Module to find pascal triangle"""


def pascal_triangle(n):
    """Initialize triangle list to store rows"""
    triangle = []


    if n <= 0:
        return triangle

    for i in range(n):
        row = []

        for j in range(i + 1):
            coefficient = factorial(i) // (factorial(j) * factorial(i - j))
            row.append(coefficient)

        triangle.append(row)

    return triangle


def factorial(num):
    """Factorial helper function"""
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
