#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number > 5:
    print("The last digit of {:d} is {:d} and is greater than 5".format(number, number % 10))
elif number == 0:
    print("The last digit of {:d} is {:d} and is 0".format(number, number % 10))
elif number < 6 & number != 0:
    print("The last digit of {:d} is {:d} and is 6 and not 0".format(number, number % 10 == 6))
