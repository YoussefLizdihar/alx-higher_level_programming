#!/usr/bin/python3

def print_last_digit(number):
    number = abs(number)
    ld = number % 10
    print(ld, end"")
    return ld
