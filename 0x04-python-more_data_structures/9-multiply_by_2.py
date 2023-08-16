#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary.copy()
    for item in b_dictionary:
        b_dictionary[item] *= 2
    return b_dictionary
