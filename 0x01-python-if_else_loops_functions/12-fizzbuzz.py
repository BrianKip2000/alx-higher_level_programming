#!/usr/bin/python3

def fizzbuzz():
    """Fizzbuz is a ftn that prints numbers fom 0 to 100
    if numbers are divisible by 3, it prints fizz
    for multiples of 5 it prints buzz
    for both multiples of 3 and 5 it prints fizzbuzz"""
    for num in range(1, 101):
        if (num % 3 == 0) and (num % 5 == 0):
            print("FizzBuzz")
        elif (num % 5 == 0):
            print("Buzz")
        elif (num % 3 == 0):
            print("Fizz")
        else:
            print(num)
