#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    tmp = len(argv) - 1
    i = 0
    for n in range(tmp):
        i = i + argv[n + 1]
    print("{}".format(i))
