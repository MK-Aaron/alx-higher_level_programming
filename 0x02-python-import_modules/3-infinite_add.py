#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sum = 0
    arg = len(sys.argv)

    for i in range(1, arg):
        sum += int(sys.argv[i])
    print(f"{sum}")
