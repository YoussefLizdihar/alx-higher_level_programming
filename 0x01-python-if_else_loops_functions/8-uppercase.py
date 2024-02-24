#!/usr/bin/python3

def uppercase(str):
    g = ""
    for j in range(str):
        if (ord('a') <= ord(j) <= ord('z')):
            x = ord(j) - 32
            y = chr (x)
            print(y, end="")
        else:
            print(j, end="")
    print()
