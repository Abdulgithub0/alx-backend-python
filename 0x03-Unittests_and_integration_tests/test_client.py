#!/usr/bin/env python3
"""unittest test module for client.py program
"""
from client import GithubOrgClient
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
import client


class TestGithubOrgClient(unittest.TestCase):
    """test all implemented features in GithubOrgClient class
    """
    @parameterized.expand([
            ("google"),
            ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, test_org_name, m_get_json):
        """test org method"""
        # m_get_json.return_value = {"org_present": True}
        result = GithubOrgClient(test_org_name)
        arg = f'https://api.github.com/orgs/{test_org_name}'
        res = result.org()
        # self.assertEqual(res, {"org_present": True})
        m_get_json.assert_called_once_with(arg)
