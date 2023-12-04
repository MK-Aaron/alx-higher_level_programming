#!/usr/bin/python3
"""Function to print a string"""


def print_list_integer(my_list=[]):
    """
    Print a list of intergers.
    args:
        my_list(list): List to print
    Returns:
        Nothing
    """
    for i in list(my_list):
        print(f"{i:d}")
