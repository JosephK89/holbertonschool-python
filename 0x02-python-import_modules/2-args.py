#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = len(sys.argv)
    if x == 1:
        print("0 arguments.")
    elif x == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(x - 1))
    for i in range(1, x):
        print("{}: {}".format(i, sys.argv[i]))
