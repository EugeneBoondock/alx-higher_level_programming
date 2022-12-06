#!/usr/bin/python3

import sys

from add_0 import add

if __name__ == "__main__":

    a = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    b = int(sys.argv[2]) if len(sys.argv) > 2 else 2

    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))
