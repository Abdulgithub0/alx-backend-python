#!/usr/bin/env python3
"""unittest for utils.py program
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
import utils


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
    """
    Defines tests for get_json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str,
                      test_payload: Dict[str, bool]) -> None:
        """
        test if get_json return correct output
        """
        config = {'return_value.json.return_value': test_payload}
        with patch('requests.get', autospec=True, **config) as mockRequestGet:
            self.assertEqual(get_json(test_url), test_payload)
            mockRequestGet.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """test memoize function
    """
    def test_memoize(self):
        """mock memoized function in utils
        """

        class TestClass:
            """nested class
            """
            def a_method(self):
                """just return 42"""
                return 42

            @memoize
            def a_property(self):
                """call a method"""
                return self.a_method()
        with unittest.mock.patch.object(TestClass, "a_method") as mock_obj:
            instan = TestClass()
            instan.a_property()
            instan.a_property()
            mock_obj.assert_called_once()
