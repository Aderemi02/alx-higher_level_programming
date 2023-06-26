#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        result = fct(*args)
    except Exception as num:
        stderr.write("Exception: {}\n".format(num))
        result = None
    return (result)
