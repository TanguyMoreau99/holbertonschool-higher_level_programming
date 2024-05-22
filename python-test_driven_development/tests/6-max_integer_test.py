#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_one_negative(self):
        self.assertEqual(max_integer([1, -2, 3, 4]), 4)

    def test_only_negatives(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        self.assertEqual(max_integer([3]), 3)

    def test_identical_elements(self):
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_mixed_integers_floats(self):
        self.assertEqual(max_integer([1, 2.2, 3, 4.4]), 4.4)

    def test_strings(self):
        self.assertEqual(max_integer(["a", "b", "c", "d"]), "d")

    def test_string_mixed_with_integers(self):
        with self.assertRaises(TypeError):
            max_integer([1, "a", 3, "d"])

if __name__ == '__main__':
    unittest.main()
