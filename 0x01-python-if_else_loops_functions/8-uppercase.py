#!/usr/bin/python3

def uppercase(str):
    g = ""
    for j in range(str):
        if (ord('a') <= ord(j) <= ord('z')):
            x = ord(ch) - 32
            y = chr (x)
            g = g + y
            print(g)
        else:
            print(j)
