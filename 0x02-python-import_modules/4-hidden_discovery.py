#!/usr/bin/python3

import importlib

if __name__ == "__main__":
    module = importlib.import_module("hidden_4")

    names = dir(module)

    print("{}".format("hidden_4"))
    for name in names:
        print(name)
