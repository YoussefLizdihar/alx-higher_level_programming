#!/usr/bin/python3

def fizzbuzz():
    print("1 2 3", end=" ")
    for a in range (5, 101):
        if (a % 3) == 0:
            if (a % 5) == 0:
                print("FizzBuzz", end=" ")
            print("Fizz", end=" ")
        elif (a % 5) == 0:
            print("Buzz", end=" ")
        else:
            print(a, end=" ")
