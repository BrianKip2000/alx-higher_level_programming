#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        # If so, return the same list unchanged
        return my_list

    # Initialize an empty list to store the modified list
    modified_list = []

    # Iterate through the elements of the original list
    for i in range(len(my_list)):
        # Skip the element at the specified index (idx)
        if i != idx:
            # Append elements other than the one at idx to the modified list
            modified_list.append(my_list[i])

    return modified_list
