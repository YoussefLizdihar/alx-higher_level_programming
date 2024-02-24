#!/usr/bin/python3

def uppercase(str):
    for j in str:
        if (ord('a') <= ord(j) <= ord('z')):
            print(chr(ord(c) - 32), end="")
        else:
            print(j, end="")
    print()
