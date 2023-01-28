#!/usr/bin/env python3
"""test_utils
"""
import unittest
from parameterized import parameterized
method = __import__("utils").access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Class that holds tests
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), 2),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test that the method returns what it is supposed to
        """
        self.assertEqual(method(nested_map, path), expected)

if __name__ == '__main__':
    unittest.main()
