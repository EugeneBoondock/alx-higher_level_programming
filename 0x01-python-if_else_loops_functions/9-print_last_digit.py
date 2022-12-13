#!/usr/bin/python3
def print_last_digit(number):
    exe = 1
    last = abs(number) % 10
    print("{}".format(last), end="")

    exe = 0
    if number < 0:
        number *= -1
        print("{:d}".format(last), end='')

        return last
