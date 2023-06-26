#!/usr/bin/python3
def safe_function(fct, *args):
    import sys.stderr as stderr
    try:
        result = fct(*args)
    except Exception as num:
        stderr.write("Exception: {}\n".format(num))
        result = None
    return (result)
