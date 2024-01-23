#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    try:
        while n < x:
            if type(my_list[n]) == int:
                print("{:d}".format(my_list[n]), end="")
                n += 1
            else:
                n += 1
                continue
        print()
    except IndexError:
        None
    return n
        
