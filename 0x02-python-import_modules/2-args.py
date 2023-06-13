#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) < 2:
        print("0: arguments.")
    elif len(argv) < 3:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(argv) - 1))
    for i in range(len(argv)):
        print("{}: {}".format(i, argv[i]))
