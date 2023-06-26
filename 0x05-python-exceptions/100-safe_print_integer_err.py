#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr
    try:
        print("{:d}".format(value))
    except Exception as num:
        stderr.write("Exception: {}\n".format(num))
        return (False)
    else:
        return (True)
