#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for dic_key in sorted(a_dictionary.keys()):
        print("{}: {}".format(dic_key, a_dictionary[dic_key]))
