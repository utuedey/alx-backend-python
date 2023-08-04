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
        self.assertEqual(github_org_client, response)

        mocked_func.assert_called_once_with(
            f"https://api.github.com/orgs/{org}")
