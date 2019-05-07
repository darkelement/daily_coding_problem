#!/bin/python

from solution import Node, serialize, deserialize
import unittest

class Test(unittest.TestCase):

    def test_simple_serialization(self):
        node = Node('root', Node('left', None, None), None)
        expectation = '[(root)[(left)[][]][]]'
        self.assertEqual(serialize(node), expectation)

    def test_problem_serialization(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        expectation = '[(root)[(left)[(left.left)[][]][]][(right)[][]]]'
        self.assertEqual(serialize(node), expectation)

    def test_empty_deserialization(self):
        string = '[]'
        expectation = None
        self.assertEqual(deserialize(string), expectation)

    def test_simple_deserialization(self):
        string = '[(root)[(left)[][]][]]'
        expectation = Node('root', Node('left', None, None), None)
        self.assertEqual(deserialize(string), expectation)

    def test_problem_deserialization(self):
        string = '[(root)[(left)[(left.left)[][]][]][(right)[][]]]'
        expectation = Node('root', Node('left', Node('left.left')), Node('right'))
        self.assertEqual(deserialize(string), expectation)

unittest.main()

