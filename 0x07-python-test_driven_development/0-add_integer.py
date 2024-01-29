#!/usr/bin/python3
def add_integer(a, b=98):
    if not isintance(a, (int, float))
        raise TypeError("a must be an integer")
    if not isintance(b, (int, float))
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.tsts("tests/0-add_integer.txt")
