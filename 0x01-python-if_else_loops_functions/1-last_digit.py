#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

output = number % 10
if output > 6:
    print(f"Last digit of {number} is {output} and is geater than 5")
elif output < 5:
    print(f"Last digit of {number} is {output} and is less than 6")
else:
    print(f"Last digit of {number} is {output} and is zero")
