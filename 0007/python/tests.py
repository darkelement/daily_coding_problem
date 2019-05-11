#!/bin/python

import solution
import unittest

class Test(unittest.TestCase):

    def test_example_1(self):
        """Check example #1 from the problem."""
        self.assertEqual(solution.solve('111'), 3)

    def test_example_2(self):
        """Check example #2 from the problem."""
        self.assertEqual(solution.solve('001'), 0)

    def test_1234321(self):
        """Test message '1234321'"""

        # 1, 2, 3, 4, 3, 2, 1
        # 1, 2, 3, 4, 3, 21
        # 1, 23, 4, 3, 2, 1
        # 12, 3, 4, 3, 2, 1
        # 12, 3, 4, 3, 21
        # 1, 23, 4, 3, 21

        self.assertEqual(solution.solve('1234321'), 6)

    def test_20212324(self):
        """Test message '20212324'"""

        # 20, 21, 23, 24
        # 20, 21, 23, 2, 4
        # 20, 21, 2, 3, 24
        # 20, 21, 2, 3, 2, 4
        # 20, 2, 1, 23, 24
        # 20, 2, 1, 23, 2, 4
        # 20, 2, 1, 2, 3, 24
        # 20, 2, 1, 2, 3, 2, 4
        # 20, 2, 12, 3, 24
        # 20, 2, 12, 3, 2, 4

        self.assertEqual(solution.solve('20212324'), 10)

unittest.main()

