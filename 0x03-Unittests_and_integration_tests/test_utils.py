#!/usr/bin/env python3
"""unittest for utils.py program
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """test all methods define in utils module
    """
    @parameterized.expand([
            ({"a": 1}, "a", 1),
            ({"a": {"b": 2}}, "a", {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, _map, path, expected):
        """assert if access_nested_map return correct output"""
        result = access_nested_map(_map, path)
        self.assertEqual(result, expected)
