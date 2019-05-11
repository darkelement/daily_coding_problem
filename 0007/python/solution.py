#!/bin/python

def solve(message):
    def count1(message, position):
        return count(message, position + 1)

    def count2(message, position):
        if not (position < len(message)):
            return 0

        c = message[position]
        if c in {'0', '1', '2', '3', '4', '5', '6'}:
            return count(message, position + 1)
        else:
            return 0

    def count(message, position):
        if position == len(message):
            return 1

        if not (position < len(message)):
            return 0

        c = message[position]

        if c == '0':
            return 0

        elif c == '1':
            return count(message, position + 1) + count1(message, position + 1)

        elif c == '2':
            return count(message, position + 1) + count2(message, position + 1)

        elif c in {'3', '4', '5', '6', '7', '8', '9'}:
            return count(message, position + 1)

    return count(message, 0)

