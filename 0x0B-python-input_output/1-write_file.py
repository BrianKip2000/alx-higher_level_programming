#!/usr/bin/python3
"""Module to create a file if it does not exist. Write contents to the file"""


def write_file(filename="", text=""):
    """Function to write file using write()"""
    with open(filename, mode='w', encoding='UTF-8') as file1:
        file1.write(text)
        return len(text)
    