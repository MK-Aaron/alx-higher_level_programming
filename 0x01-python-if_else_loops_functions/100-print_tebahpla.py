#!/usr/bin/python3
check = True
for i in range(122, 96, -1):
    if check:
        a = i
    else:
        a = i - 32
    print("{:s}".format(chr(a)), end="")
