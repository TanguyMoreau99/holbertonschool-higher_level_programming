#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max_nbr = my_list[0]

    for nbr in my_list[1:]:
        if nbr > max_nbr:
            max_nbr = nbr

    return max_nbr
