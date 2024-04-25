"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """Python class for unittesting"""
    def test_is_max_at_the_end(self):
        """Class method for testing max integer
        Args:
            test_is_max: tests for maximum result"""
        self.assertEqual(max_integer([1,8,19,28]), 28)
    def test_max_at_begining(self):
        """Method with max number at the beginning"""
        self.assertEqual(max_integer([99, 90, 83]), 99)

    def test_max_at_middle(self):
        """Method with max number at the middle"""
        self.assertEqual(max_integer([1, 2, 0]), 2)

    def test_max_with_negative(self):
        """returns maximum of negatives"""
        self.assertEqual(max_integer([-3, -2, -1]), (-1))

    def test_max_with_equal(self):
        """test with equal numbers"""
        self.assertEqual(max_integer([4, 4, 4]), 4)

    def test_max_with_string(self):
        """test with numbers with strings"""
        self.assertEqual(max_integer([3, '4', 5, 25, 'Bro']), 25)

    def test_max_without_numbers(self):
        """test with empty module"""
        self.assertEqual(max_integer([]), None)
    