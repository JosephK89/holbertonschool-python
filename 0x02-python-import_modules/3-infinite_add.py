#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = len(sys.argv)
    sum = 0
    for i in range (x):
        if i >= 1:
            sum += int(arvg[i + 1])
    print("{:d}".format(sum))
