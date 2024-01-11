#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return
    j = 0
    i = None
    new_dict = a_dictionary.copy()
    for y, x in new_dict.items():
        if x > j:
            j = x
            i = y
    return i
