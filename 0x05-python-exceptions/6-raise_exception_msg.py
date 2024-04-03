#!usr/bin/python3
def raise_exception_msg(message=""):
    try:
        geek = input()
        print(geek)
    except NameError:
        return message
