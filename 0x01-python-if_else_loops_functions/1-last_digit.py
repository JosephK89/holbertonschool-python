#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    ld = (abs(number)%10) * -1
else:
    ld = number%10
print("Last digit of {:d} is {:d} and is ".format(number, ld), end="")
if ld == 0:
    print("0")
elif ld > 5:
    print("greater than 5")
elif ld < 6 and ld != 0:
    print("less than 6 and not 0")
