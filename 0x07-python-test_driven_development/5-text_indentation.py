#!/usr/bin/python3

"""Module to print text that is not a string"""


def text_indentation(text):
    """Function to print . , ? at the end
    Args:
        text(str): text shoul be a string only
    Raises:
        TypeError: with exception message 'text must be a string'"""
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
