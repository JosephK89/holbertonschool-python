#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    else:
        num = 0
        deno = 0
        for i in my_list:
            num += i[0]*i[1]
            dem += i[1]
        return (num / dem)
