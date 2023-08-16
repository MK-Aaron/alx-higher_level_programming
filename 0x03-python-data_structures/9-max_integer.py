#!/usr/bin/python3

def max_interger(my_list=[]):
    if my_list:
        max = my_list[0]
        for n in my_list[1:]:
            if n > max:
                max = n
        return max
