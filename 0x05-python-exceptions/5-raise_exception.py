#!/usr/bin/python3
def raise_exception():
    try:
        #Perfom an impossible operation
        return None +2
    except TypeError:
        raise TypeError("Mission Impossible")
