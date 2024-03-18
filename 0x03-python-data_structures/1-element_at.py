#!/usr/bin/python3
""" A function that etrieves all elements in a list"""
def element_at(my_list, idx):
    for num in idx:
        if num < 0:
            return None
        elif num > len(my_list):
            return None
        else:
            retun my_list[idx]
