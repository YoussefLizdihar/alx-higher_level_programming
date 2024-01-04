#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv) - 1
    print("{:d} argument{}:".format(args, 's' if args != 1 else ''), end='')
    if args == 0:
        print(".")
    else:
        print()
    for i in range(1, args + 1):
        print("{:d}: {}".format(i, argv[i]))

