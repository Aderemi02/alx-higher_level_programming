#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    import calculator_1 as calc
    opts = {'+': calc.add, '-': calc.sub, '*': calc.mul, '/': calc.div}
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    c = argv[2]
    if c not in '+-/*':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    result = opts[c](a, b)
    print('{:d} {:s} {:d} = {:d}'.format(a, c, b, result))
