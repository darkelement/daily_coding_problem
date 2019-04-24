#!/bin/python

def naive(numbers, k):
    """
    This is a naive solution. For every element in `numbers` we iterate over `numbers` once again
    searching for numbers that will add up to `k`. Doing that we skip adding numbers to themselves.
    """

    for i, a in enumerate(numbers):
        for j, b in enumerate(numbers):
            if (i != j) and ((a + b) == k):
                return True
    return False

def one_pass(numbers, k):
    """
    This is an approach with one pass. We search two numbers that will add up to `k` so for any
    given number `n` we need to know if `k - n` is also in the `numbers`. We prepare a set
    `visited` of visited numbers and add numbers to it as we iterate over them. If `k - n` is in the
    set we return `True`. If never found - return `False`.
    """

    visited = set()
    for number in numbers:
        complement = k - number
        if complement in visited:
            return True
        visited.add(number)
    return False

