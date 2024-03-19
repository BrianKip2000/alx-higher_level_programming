#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        # If so, return the same list unchanged
        return my_list

    # Initialize an empty list to store the modified list
    new_list = []

    # Iterate through the elements of the original list
    del new_list[idx]
    return new_list
