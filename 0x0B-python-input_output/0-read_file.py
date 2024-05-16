#!/usr/bin/python3


def read_file(filename=""):
    with open("my-file_0.txt", mode="r", encoding="UTF-8") as UTF8:
        read_file = UTF8.read()

        print(read_file)
