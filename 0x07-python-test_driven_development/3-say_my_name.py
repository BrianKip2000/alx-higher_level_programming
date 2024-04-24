#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """Function to input first name and last name
    args:
        @first_name: first user name
        @last_name: last user name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
