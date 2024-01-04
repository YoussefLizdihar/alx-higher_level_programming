#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    tmp = len(sys.argv) - 1
    if tmp == 0:
        print("0 arguments.")
    elif tmp == 1:
        print("1 arguments.")
    else:
        print("{} arguments:".format(tmp))
    for n in range(tmp):
        print("{}: {}".format(n + 1, sys.argv[n + 1]))
