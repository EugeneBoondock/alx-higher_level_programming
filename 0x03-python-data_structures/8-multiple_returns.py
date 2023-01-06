#!/usr/bin/python3

def multiple_returns(sentence):
    return (sentence[0] if sentence != "" else None, len(sentence))
