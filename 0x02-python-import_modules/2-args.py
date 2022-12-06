#!/usr/bin/python3

import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    args = sys.argv[1:]

    print("Number of arguments: {}".format(num_args))
    print("Arguments: {}".format(args))
