#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    listcopy = my_list.copy()
    if len(my_list) - 1 < idx or idx < 0:
        return my_list
    else:
        listcopy[idx] = element
        return listcopy
