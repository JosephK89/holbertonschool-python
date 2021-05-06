#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        f = fct(*args)
        return f
    except Exception as ex:
        print("Exception:", ex, file=sys.stderr)
        return None
