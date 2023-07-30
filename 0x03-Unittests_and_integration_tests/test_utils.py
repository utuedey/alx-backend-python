#!/usr/bin/env python3
"""test cases for utils module"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for the utils functions"""

    # Define the test data as a list of tuples:
    # (input_a, input_b, expected_result)
    test_parameters = (
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        )

    test_parameter_2 = (
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        )

    @parameterized.expand(test_parameters)
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Test case for the access_nested_map function"""
        res = access_nested_map(nested_map, path)
        self.assertEqual(res, expected_result)

    @parameterized.expand(test_parameter_2)
    def test_access_nested_map_exception(self, nested_map, path):
        """Test case for the access_nested_map exceptions"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


if __name__ == "__main__":
    unittest.main()
