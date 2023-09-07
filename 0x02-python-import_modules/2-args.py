#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg = len(sys.argv)

    if arg == 1:
        print(f"0 arguments.")
    else:
        print(f"{arg - 1} argument", end='')
        if arg == 2:
            print(":")
        else:
            print("s:")
        for i in range(1, arg):
            print("{}: {}".format(i, sys.argv[i]))
