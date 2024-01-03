#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    p = number % 10
    print("Last digit of",number, "is",p,end=" ")
    if p > 5:
        print("and is greater than 5")
    elif p == 0:
        print("and is 0")
elif number < 0:
    num = -number
    n = -(num % 10)
    print("Last digit of",number, "is",n,end=" ")
    if n < 0:
        print("and is less than 6 and not 0")
    elif n == 0:
        print("and is 0")
