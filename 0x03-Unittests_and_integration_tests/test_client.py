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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """test for the public_repos method"""
        test_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos",
            "repos": [
                {
                 "id": 7776515,
                 "name": "cpp-netlib",
                 "private": False,
                 "owner": {
                        "login": "google",
                        "id": 1342004,
                        },
                 "fork": True,
                 "url": "https://api.github.com/repos/google/cpp-netlib",
                 "created_at": "2013-01-23T14:45:32Z",
                 "updated_at": "2019-11-15T02:26:31Z",
                 "has_issues": False,
                 "forks": 59,
                 "default_bracnch": "master",
                    },
                {
                 "id": 7968417,
                 "name": "dagger",
                 "private": False,
                 "owner": {
                        "login": "google",
                        "id": 1342004,
                        },
                 "fork": True,
                 "url": "https://api.github.com/repos/google/dagger",
                 "created_at": "2013-02-01T23:14:14Z",
                 "updated_at": "2019-12-03T12:39:55Z",
                 "has_issues": True,
                 "forks": 1741,
                 "default_bracnch": "master",
                    },
                ]
            }
        mock_get_json.return_value = test_payload['repos']
        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                ["cpp-netlib", "dagger"])
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
