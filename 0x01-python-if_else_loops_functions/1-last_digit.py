#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)
last_d = int(number_str[-1])
i = "Last digit of"

if last_d > 5:
    print("{} {} is {} and is greater than 5".format(i, number, last_d))

elif last_d < 6 and last_d != 0:
    print("{} {} is {} and is less than 6 and not 0".format(i, number, last_d))

else:
    print("{} {} is {} and is 0".format(, number, last_d))
