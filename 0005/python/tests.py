#!/bin/python

from solution import cons, car, cdr
import unittest

class Test(unittest.TestCase):

    def test_car(self):
        self.assertEqual(car(cons(3, 4)), 3)
        self.assertEqual(car(cons(7, 2)), 7)

    def test_cdr(self):
        self.assertEqual(cdr(cons(3, 4)), 4)
        self.assertEqual(cdr(cons(7, 2)), 2)

unittest.main()

