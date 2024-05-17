#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    output = number % 10
else:
    output = abs(number) % 10

if number < 0:
    output = -output

if output > 6:
    print(f"Last digit of {number} is {output} and is greater than 5")
elif output < 5:
    print(f"Last digit of {number} is {output} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {output} and is 0")
