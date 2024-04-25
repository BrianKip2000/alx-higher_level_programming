"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """Python class for unittesting"""
    def test_is_max(self):
        """Class method for testing max integer
        Args:
            test_is_max: tests for maximum result"""
        self.assertEqual(max_integer.max_integer([1,8,19,28]), 28)
        