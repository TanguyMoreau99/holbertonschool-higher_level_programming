#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    nb_printed = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            nb_printed += 1

        except (TypeError, ValueError):
            pass

    print()
    return nb_printed
