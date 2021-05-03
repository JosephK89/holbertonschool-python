#!/usr/bin/python3
def no_c(my_string):
    my_string=''.join(i for i in my_string if not i in "cC")
    return my_string
