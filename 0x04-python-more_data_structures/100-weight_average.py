#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    else:
        a = 0
        b = 0
        for tup in my_list:
            a += tup[0] * tup[1]
            b += tup[1]
        return a/b
