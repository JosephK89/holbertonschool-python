#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = len(argv)
    print("{:d} {:s}{:s}".format(x - 1, "argument" if x == 1 else "arguments","." if x == 0 else ":"))
    for i in range(x):
        if i > 0:
            print("{:d}: {:s}".format(i, arvg[i])
