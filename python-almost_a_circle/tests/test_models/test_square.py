#!/usr/bin/python3
"""Defines tests for 'Square' class"""


import unittest
from models.square import Square

class TestSquareMethods(unittest.TestCase):

    def setUp(self):
        """Set up a default Square instance for testing"""
        self.default_square = Square(size=3, id=1)

    def test_default_values(self):
        """Test default values of the Square instance"""
        self.assertEqual(self.default_square.size, 3)
        self.assertEqual(self.default_square.width, 3)
        self.assertEqual(self.default_square.height, 3)
        self.assertEqual(self.default_square.x, 0)
        self.assertEqual(self.default_square.y, 0)
        self.assertEqual(self.default_square.id, 1)

    def test_setters(self):
        """Test the setter for size"""
        # Test valid values
        self.default_square.size = 5
        self.assertEqual(self.default_square.size, 5)
        self.assertEqual(self.default_square.width, 5)
        self.assertEqual(self.default_square.height, 5)

        # Test invalid values
        with self.assertRaises(ValueError):
            self.default_square.size = -1

        with self.assertRaises(TypeError):
            self.default_square.size = "invalid"