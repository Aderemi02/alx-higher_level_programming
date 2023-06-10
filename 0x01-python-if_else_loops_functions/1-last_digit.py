#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    result = number % 10
    if result == 0:
        print(f"Last digit of {number} is {result} and is 0")
elif number < 0:
    number2 = number * -1
    result = number2 % 10
if result > 5:
    print(f"Last digit of {number} is {result} and is greater than 5")
elif result < 6:
    print(f"Last digit of {number} is {result} and is lesser than 6 and not 0")
