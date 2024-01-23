#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    try:
        while n is not x:
            print(my_list[i], end="")
            n = n + 1
        print()
    except IndexError:
        None
        print()
    return n
        
