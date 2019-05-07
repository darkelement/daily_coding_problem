#!/bin/python

# Node class from the problem with
#  - comparison operator for comparison in tests and
#  - printable representation for debugging
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        if other is not None:
            return self.val == other.val \
               and self.left == other.left \
               and self.right == other.right
        else:
            return False

    def __repr__(self):
        return serialize(self)

# The serialized representation is very simple so that deserialization algorithm may be simple,
# e.g. all element markers are single characters and no white spaces are allowed.
def serialize(node):
    """
    Serializes the `Node` class.

    Every node is braced by square parenthesis (`[`, `]`) and every value by round parenthesis ('(',
    ')'). Empty nodes are represented by empty square brackets `[]`. The elements are placed in
    order:
     - value,
     - left node,
     - right node
    without any white spaces between.

    For example
    ```
        Node('root', Node('left', None, None), None)
    ```
    will be serialized to `[(root)[(left)[][]][]]`.

    The characters are not escaped, so character `)` is not allowed in values.
    """

    if node is not None:
        return '[({}){}{}]'.format(node.val, serialize(node.left), serialize(node.right))
    else:
        return '[]'

def deserialize(string):
    """Deserializes Node serialized with `serialize`."""

    class Deserializer:
        def __init__(self, string):
            self.string = string
            self.pos = 0

        def deserialize(self):
            """Deserializes node."""

            self._expect('[')

            current = self.string[self.pos]
            self.pos += 1
            if current == '(':
                val = self._deserialize_value()
                left = self.deserialize()
                right = self.deserialize()
                self._expect(']')
                return Node(val, left, right)

            elif current == ']':
                return None

            else:
                self._fail(['(', ']'], current)

        def _deserialize_value(self):
            """Deserializes value."""

            begin = self.pos
            while self.string[self.pos] != ')':
                self.pos += 1
            end = self.pos
            self.pos += 1
            return self.string[begin:end]

        def _expect(self, expected):
            """
            Checks if the character on the current position is equal to `expected`. If so, the
            current position is moved forward by one, otherwise an exception is raised.
            """

            found = self.string[self.pos]
            if found != expected:
                self._fail([expected], found)
            self.pos += 1

        def _fail(self, expected, found):
            """Formats and raises an exception."""

            if len(expected) == 1:
                msg = 'Expected "{}", found "{}" (at position {})' \
                    .format(expected[0], found, self.pos)
            else:
                expected = ', '.join(['"' + exp + '"' for exp in expected])
                msg = 'Expected one of {}, found "{}" (at position {})' \
                    .format(expected, found, self.pos)
            raise Exception(msg)

    return Deserializer(string).deserialize()

