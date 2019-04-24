#!/bin/python

import solution
import time
import random

# "Naive" solution iterates over numbers and then searches a complement number in a list. "One pass"
# solution iterates over numbers and searches a complement number in a set. Sets are much faster
# than lists when it comes to search so we expect the "one pass" algorithm to be much faster.

def measure_time():
    k = 10
    numbers = [random.randint(10, 100) for _ in range(0, 10000)]
    numbers.append(4)
    numbers.append(6)

    def measure(name, function):
        start = time.time()
        assert(function(numbers, k) == True)
        end = time.time()
        print('Solution found after {:8.4f} seconds using "{}" algorithm'.format(end - start, name))

    measure('naive', solution.naive)
    measure('one pass', solution.one_pass)

measure_time()

