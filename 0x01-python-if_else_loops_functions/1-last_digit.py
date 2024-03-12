#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if last_digit > 5:
    relation = "and is greater than 5"
elif last_digit == 0:
    relation = "and is zero"
else:
    relation = "and is less than 6 and not 0"
print("last_digit of", number, "is", last_digit, relation)
