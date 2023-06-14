#!/usr/bin/python3
if __name__ = "__main__":
    from sys import argv, exit
    if len(argv) - 1 != 3:
        print("./100-my_calculator.py <a> operator <b>")
        exit(1)
    operators = {"+": add, "-": sub, "*": mul, "/": div}
    op = list(operator.keys())
    if argv[2] not in op:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    c = argv[2]
    result = operator[c](a, b)
    print("{} {} {} = {}".format(a, c, b, result))
