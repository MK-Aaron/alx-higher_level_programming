#!/usr/bin/python3

def uppercase(str):
    for i in list(str):
        if i > 96 and i < 123:
           i = i - 32
        print(i, end='')
    print("\n")
