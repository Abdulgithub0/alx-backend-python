#!/usr/bin/env python3
"""unittest test module for client.py program
"""
from client import GithubOrgClient
import unittest
from unittest.mock import patch, Mock, PropertyMock
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
        result = GithubOrgClient(test_org_name)
        arg = f'https://api.github.com/orgs/{test_org_name}'
        result.org()
        m_get_json.assert_called_once_with(arg)

    @parameterized.expand([
            ("org_name", {"repos_url": "https://api.github.com/orgs/org_name"})
    ])
    def test_public_repos_url(self, test_org_name, test_org_result):
        """test public_repos_url method"""
        with patch("client.GithubOrgClient.org",
                   PropertyMock(return_value=test_org_result)):
            repos = GithubOrgClient(test_org_name)._public_repos_url
            self.assertEqual(repos, test_org_result["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """mock test public_repo method"""
        test_org_name = [{"name": "google"}, {"name": "github"}]
        mock_get_json.return_value = test_org_name
        with patch("client.GithubOrgClient._public_repos_url",
                   PropertyMock(return_value="http://api.com/org/org")) as m:
            client_instan = GithubOrgClient("google")
            result = client_instan.public_repos()
            match_names = [names['name'] for names in test_org_name]
            self.assertEqual(result, match_names)
            mock_get_json.assert_called_once_with("http://api.com/org/org")
            m.assert_called_once()

    @parameterized.expand([
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, in_params, out_params):
        """test has_license method"""
        bools = GithubOrgClient.has_license(repo, in_params)
        self.assertEqual(bools, out_params)
