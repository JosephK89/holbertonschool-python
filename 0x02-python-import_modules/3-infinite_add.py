#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = len(argv) - 1
    sum = 0
    for i in range (x):
        sum += int(arvg(i + 1))
    print("{:d}".format(sum))
