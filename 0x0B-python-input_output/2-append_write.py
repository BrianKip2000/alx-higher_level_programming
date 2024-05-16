#!/usr/bin/python3
"""Module to append text file and return number of char"""


def append_write(filename="", text=""):
    """Function to append text"""
    with open(filename, mode='a', encoding='utf-8') as file2:
        file2.write(text)
        return len(text)
