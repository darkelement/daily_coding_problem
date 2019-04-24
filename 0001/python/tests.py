#!/bin/python

import solution
import unittest

class TestData:
    def __init__(self, numbers, k, result):
        self.numbers = numbers
        self.k = k
        self.result = result

TEST_DATA = (
        # Simple negative cases
        TestData((1, 2, 3, 4, 5, 6, 7), 1000, False),
        TestData((100, 200, 300, 400, 500, 600, 700), 1, False),

        # Make sure a number is not matched with itself
        TestData((100, 200, 3, 400, 500, 600, 700), 6, False),

        # Positive cases
        TestData((10, 15, 3, 7), 17, True),
        TestData((1, 2, 3, 4, 5, 6, 7), 9, True),
    )

class TestStringMethods(unittest.TestCase):

    def test_naive(self):
        for data in TEST_DATA:
            assert(solution.naive(data.numbers, data.k) == data.result)

    def test_one_pass(self):
        for data in TEST_DATA:
            assert(solution.one_pass(data.numbers, data.k) == data.result)

unittest.main()

