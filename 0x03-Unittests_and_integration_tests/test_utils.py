#!/usr/bin/env python3
"""test_utils
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch
access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json


class TestAccessNestedMap(unittest.TestCase):
    """Class that holds tests
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test that the method returns what it is supposed to
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ('a',)), ({'a': 1}, ('a', 'b'))])
    def test_access_nested_map_exception(self, nested_map, path):
        """test KeyError in method
        """
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
        err_raised = None
        for i in path:
            if i not in nested_map.keys():
                err_raised = i
        self.assertEqual(str(err.exception)[1], str(err_raised))


def mocked_method(*args, **kwargs):
    """mocking with requests.get
    """
    class Req:
        """mock of class Requests.get
        """
        def __init__(self, resp):
            """initializer
            """
            self.resp = resp

        def json(self):
            """mock of json()
            """
            return self.resp
        if args[0] == "http://example.com":
            return Req({"payload": True})
        elif args[0] == "http://holberton.io":
            return Req({"payload": False})


class TestGetJson(unittest.TestCase):
    """Class tests get_json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, test_url, test_payload):
        """ test get_json
        """
        with patch("requests.get", side_effect=mocked_method) as get:
            self.assertEqual(get_json(test_url), test_payload)
        get.assert_called_once()


if __name__ == '__main__':
    unittest.main()
