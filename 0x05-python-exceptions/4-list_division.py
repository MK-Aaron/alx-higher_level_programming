#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for x, y in zip(my_list_1, my_list_2):
        try:
            result = x / y
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list
