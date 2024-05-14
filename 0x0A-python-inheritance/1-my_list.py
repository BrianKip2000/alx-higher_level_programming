#!/usr/bin/python3


class MyList(list):
    """MyList class returns sorted list"""
    def print_sorted(self):
        """Prints sorted list
        Args:
        self: keyword
        """
        sorted_list = sorted(self)
        print(sorted_list)
