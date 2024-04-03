#!/usr/bin/python3
def raise_exception():
    try:
        return None + 2
    except TypeError:
        raise TypeError("Mission Impossible")
