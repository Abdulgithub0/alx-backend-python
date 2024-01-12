#!/usr/bin/env python3
"""unittest test module for client.py program
"""
from client import GithubOrgClient
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
import client
from fixtures import TEST_PAYLOAD


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


@parameterized_class(
        ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
        TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """implement integration test
    """
    @classmethod
    def setUpClass(cls):
        """class setup setting"""
        kwargs = {"return_value.json.side_effect": [
                 cls.org_payload, cls.repos_payload,
                 cls.org_payload, cls.repos_payload]
        }
        cls.get_patcher = patch("requests.get", **kwargs)
        cls.mock_obj = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """stop the patch"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Integrated test for public repos method"""
        instan = GithubOrgClient("github")
        self.assertEqual(instan.org, self.org_payload)
        self.assertEqual(instan.repos_payload, self.repos_payload)
        self.assertEqual(instan.public_repos(), self.expected_repos)
        self.mock_obj.assert_called()

    def test_public_repos_with_license(self):
        """ Integration test for public repos with License """
        test_class = GithubOrgClient("google")
        self.assertEqual(test_class.public_repos("empty"), [])
        self.assertEqual(test_class.public_repos("apache-2.0"),
                         self.apache2_repos)
        self.mock_obj.assert_called()
