#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    listcopy = my_list.copy()
    if len(listcopy) - 1 < idx or idx < 0:
        return listcopy
    else:
        listcopy[idx] = element
        return listcopy
