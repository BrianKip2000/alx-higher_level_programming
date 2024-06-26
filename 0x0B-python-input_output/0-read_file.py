#!/usr/bin/python3
"""Module to read a file using read()"""


def read_file(filename=""):
    """Function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
