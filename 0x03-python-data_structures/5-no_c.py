#!/usr/bin/python3
def no_c(my_string):
    my_string="".join(i for i in my_string if i not in "cC")
    return my_string
