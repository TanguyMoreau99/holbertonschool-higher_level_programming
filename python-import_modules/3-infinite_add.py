#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv

    infinit_sum = 0

    if len(argv) == 1:
        print("{}".format(infinit_sum))
    else:
        for index in range(1, len(argv)):
            infinit_sum += int(argv[index])
        print("{}".format(infinit_sum))
