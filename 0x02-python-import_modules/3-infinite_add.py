#!/usr/bin/python3

import sys

from add_0 import add

if __name__ == "__main__":

    sum = 0
    for i in range(1, len(sys.argv)):
        sum = add(sum, int(sys.argv[i]))

    print("{}".format(sum))           
