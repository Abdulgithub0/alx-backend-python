#!/usr/bin/env python3
"""unittest for utils.py program
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json


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

    @parameterized.expand([
            ({}, "a", "f"),
            ({"a": 1}, "d", "b")
    ])
    def test_access_nested_map_exception(self, _map, path, expected):
        """verify if exception as defined in the method is raise"""
        with self.assertRaises(KeyError) as err:
            access_nested_map(_map, path)


class TestGetJson(unittest.TestCase):
    """define unittest for get_json
    """
    @parameterized.expand([
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """test if get_json return correct output
        """
        m = unittest.mock.Mock()
        m.json.return_value = test_payload
        with unittest.mock.patch("requests.get") as req:
            req.return_value = m
            result = get_json(test_url)
            m.json.assert_called_once()
            self.assertEqual(result, test_payload)
