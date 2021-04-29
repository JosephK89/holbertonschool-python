#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = len(argv) - 1
    print("{:d} {:s}{:s}".format(x, "argument" if x == 1 else "arguments","." if x == 0 else ":"))
    for i in range(x):
        if i > 0:
            print("{:d}: {:s}".format(i, arvg(i + 1))
