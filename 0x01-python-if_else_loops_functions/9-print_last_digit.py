#!/usr/bin/python3

def print_last_digit(number):
    """Function prints last digit of number
    if number % 10= another number
    print that number
    return the number"""
    new_last = abs(number) % 10
    print(new_last, end='')
    return new_last
