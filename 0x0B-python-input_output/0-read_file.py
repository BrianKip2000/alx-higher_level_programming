#!/usr/bin/python3
"""Module to read a file using read()"""


def read_file(filename=""):
    """
    A function that reads the content of a file and prints it out.
    Parameters:
        filename (str): The name of the file to be read. Default is an empty string.
    Returns:
        None
    """
    with open("my-file_0.txt", mode="r", encoding="UTF-8") as UTF8:
        read_file = UTF8.read()

        print(read_file)
