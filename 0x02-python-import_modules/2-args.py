#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    tmp = len(argv) - 1
    if tmp == 0:
        print("0 arguments.")
    elif tmp == 1:
        print("1 argument.")
    else:
        print("{} arguments:"format(tmp))
    for n in range(tmp):
        print("{}: {}".format(n + 1, argv[n + 1]))
