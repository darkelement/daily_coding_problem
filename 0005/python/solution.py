#!/bin/python

# Typically by "pair" we mean a two-element tuple or class. In this problem "pair" is function with
# two elements captured in its environment. That function takes as argument another function, calls
# it with the two elements as arguments and then returns the value returned by that function. To
# implement `car` we have to then call the pair with a function that takes two arguments and returns
# the first one. To implement `cdr` we have to call the pair with a function that takes two
# arguments and returns the second one.

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    return pair(lambda a, b: a)

def cdr(pair):
    return pair(lambda a, b: b)

