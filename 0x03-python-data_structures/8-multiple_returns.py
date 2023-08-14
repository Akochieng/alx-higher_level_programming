#!/usr/bin/python3
def multiple_returns(sentence):
    lent = len(sentence)
    if lent == 0:
        c = None
    else:
        c = sentence[0]
    return (lent, c)
