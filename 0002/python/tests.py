#!/bin/python

import solution
import unittest

class TestData:
    def __init__(self, input_data, output_data):
        self.input_data = input_data
        self.output_data = output_data

TEST_DATA = (
        TestData([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
        TestData([3, 2, 1], [2, 3, 6]),
    )

class TestStringMethods(unittest.TestCase):

    def test_with_division(self):
        for data in TEST_DATA:
            assert(solution.with_division(data.input_data) == data.output_data)

    def test_without_division(self):
        for data in TEST_DATA:
            assert(solution.without_division(data.input_data) == data.output_data)

unittest.main()


