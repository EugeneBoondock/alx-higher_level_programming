#!/usr/bin/python3

import sys

def add(x, y):
    result = x + y
    return result

if __name__ == "__main__":
    # Check that the script was run with the x and y arguments
    if len(sys.argv) != 3:
        print("Usage: python my_script.py x y")
        exit(1)

    # Get the x and y arguments from the sys.argv list
    x = int(sys.argv[1])
    y = int(sys.argv[2])

    # Call the add() function with the x and y arguments
    result = add(x, y)
    print(result)
