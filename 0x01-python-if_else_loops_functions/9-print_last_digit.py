#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        ld = abs(number)%10 * -1
        print(ld)
    else:
        ld = number%10
        print(ld)
