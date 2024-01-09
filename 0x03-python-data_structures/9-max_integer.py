#!/usr/bin/python3
def max_integer(my_list=[]):
    temp = 0
    if not my_list:
        return
    for i in my_list:
        if i > temp:
            temp = i
    return temp
