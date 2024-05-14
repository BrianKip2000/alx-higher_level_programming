#!/usr/bin/python3
"""Locked class to make  sure that the first name is ..."""


class LockedClass:
    """LockedClass to set attribute"""
    def __setattr__(self, name, value):
        if name == 'first_name':
            super().__setattr__(name, value)
        else:
            raise AttributeError("'LockedClass' object has "
                                 "no attribute '{}'".format(name))
