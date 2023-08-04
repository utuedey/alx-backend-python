#!/usr/bin/env python3
"""
test_client module
"""
import unittest
from typing import Dict
from parameterized import parameterized

from client import GithubOrgClient

from unittest.mock import (
    MagicMock,
    patch,
    PropertyMock
    )


class TestGithubOrgClient(unittest.TestCase):
    """Test for the GithubOrgClient class"""

    test_data = (
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    )

    @parameterized.expand(test_data)
    @patch("client.get_json")
    def test_org(self, org: str, response: Dict,
                 mocked_func: MagicMock) -> None:
        """test for org method"""
        mocked_func.return_value = MagicMock(return_value=response)
        github_org_client = GithubOrgClient(org)
        self.assertEqual(github_org_client.org(), response)

        mocked_func.assert_called_once_with(
            f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self) -> None:
        """test for the public_repos_url property"""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos"
                }
            self.assertEqual(GithubOrgClient("google")._public_repos_url,
                             "https://api.github.com/users/google/repos")


if __name__ == "__main__":
    unittest.main()
