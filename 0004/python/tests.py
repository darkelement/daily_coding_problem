#!/bin/python

import solution
import unittest

class Test(unittest.TestCase):

    def test_example_1(self):
        """Check example #1 from the problem."""
        self.assertEqual(solution.solve([3, 4, -1, 1]), 2)

    def test_example_2(self):
        """Check example #2 from the problem."""
        self.assertEqual(solution.solve([1, 2, 0]), 3)

    def test_some_excessing(self):
        """Check the case when some values are bigger the length of the array."""
        self.assertEqual(solution.solve([8, 7, 2, -1, 1]), 3)

    def test_sorted_ascending(self):
        """Check the case when the result is bigger than all the elements and the array is sorted in
        an ascending order."""
        self.assertEqual(solution.solve([1, 2, 3, 4, 5]), 6)

    def test_sorted_descending(self):
        """Check the case when the result is bigger than all the elements and the array is sorted in
        an descending order."""
        self.assertEqual(solution.solve([5, 4, 3, 2, 1]), 6)

    def test_all_zeros(self):
        """Check the case when all the elements are zeros."""
        self.assertEqual(solution.solve([0, 0, 0, 0, 0]), 1)

    def test_all_ones(self):
        """Check the case when all the elements are ones."""
        self.assertEqual(solution.solve([1, 1, 1, 1, 1]), 2)

    def test_all_the_same(self):
        """Check the case when all the elements are the same value bigger the one."""
        self.assertEqual(solution.solve([3, 3, 3, 3, 3]), 1)

    def test_all_negative(self):
        """Check the case when all the elements are negative."""
        self.assertEqual(solution.solve([-1, -3, -2, -5, -8]), 1)

    def test_all_excessing(self):
        """Check the case when all the elements are bigger than the length of the array."""
        self.assertEqual(solution.solve([11, 13, 12, 15, 18]), 1)

    def test_continuous_negative_and_positive(self):
        """Check the case when elements are positive and negative without any gap."""
        self.assertEqual(solution.solve([1, -2, 2, -1, 0]), 3)

    def test_swapped(self):
        """Check the case when two elements are swapped"""
        self.assertEqual(solution.solve([3, -2, 3, 2, -2, 1]), 4)

    def test_permutation(self):
        """Check the case when two elements constitute a permutation"""
        self.assertEqual(solution.solve([-4, 1, 3, 2, -2, 1]), 4)
        self.assertEqual(solution.solve([1, 3, 2, -2, 1, -4]), 4)

unittest.main()

