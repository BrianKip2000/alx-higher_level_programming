#!/usr/bin/python3
"""Module for printing text_indentation"""


def text_indentation(text):
    """Text indentation
    Args:
        text(str): text should be string
    Raises:
        TypeError:"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    after_new_line = False
    for c in text:
        if after_new_line:
            if c == " ":
                continue
            after_new_line = False
        if c == '.' or c == '?' or c == ':':
            print(c)
            print("")
            after_new_line = True
        else:
            print(c, end="")
