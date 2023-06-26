#!/usr/bin/python3
def safe_function(fct, *args):
    import sys.stderr.write as res
    try:
        result = fct(*args)
    except Exception as num:
        res("Exception: {}\n".format(num))
        result = None
        return (result)
