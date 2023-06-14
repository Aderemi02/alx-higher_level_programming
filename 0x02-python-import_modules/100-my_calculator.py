#!/usr/bin/python3
if __name__ = "__main__":
    from sys import argv, exit
    import calculator_1 as calc
    operators = {'+': calc.add, '-': calc.sub, '*': calc.mul, '/': calc.div}
    if len(argv) != 4:
        print("./100-my_calculator.py <a> operator <b>")
        exit(1)
    op = list(operators.keys())
    a = int(argv[1])
    b = int(argv[3])
    c = argv[2]
    if c not in op:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    result = operators[c](a, b)
    print("{:d} {:s} {:d} = {:d}".format(a, c, b, result))
