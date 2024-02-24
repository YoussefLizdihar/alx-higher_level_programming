#!/usr/bin/python3

def uppercase(str):
    for j in str:
        if (ord('a') <= ord(j) <= ord('z')):
            c = ord(j) - 32
            Cc = chr(c)
            print(Cc, end="")
        else:
            print(j, end="")
    print()
