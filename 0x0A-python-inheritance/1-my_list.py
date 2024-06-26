#!/usr/bin/python3
"""Module to return a sorted list"""


class MyList(list):
    """MyList class returns sorted list"""
    def print_sorted(self):
        """Prints sorted list
        Args:
        self: keyword
        """
        sorted_list = sorted(self)
        print(sorted_list)
