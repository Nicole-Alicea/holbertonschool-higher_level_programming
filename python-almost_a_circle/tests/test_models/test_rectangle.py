#!/usr/bin/python3
"""Defines tests for the 'Rectangle' class"""


import unittest
from models.rectangle import Rectangle

class TestRectangleMethods(unittest.TestCase):

    def setUp(self):
        """Set up a default Rectangle instance for testing"""
        self.default_rect = Rectangle(width=2, height=4, id=1)

    def test_default_values(self):
        """Test default values of the Rectangle instance"""
        self.assertEqual(self.default_rect.width, 2)
        self.assertEqual(self.default_rect.height, 4)
        self.assertEqual(self.default_rect.x, 0)
        self.assertEqual(self.default_rect.y, 0)
        self.assertEqual(self.default_rect.id, 1)

    def test_setters(self):
        """Test the setters for width, height, x, and y"""
        # Test valid values
        self.default_rect.width = 5
        self.assertEqual(self.default_rect.width, 5)

        self.default_rect.height = 8
        self.assertEqual(self.default_rect.height, 8)

        self.default_rect.x = 3
        self.assertEqual(self.default_rect.x, 3)

        self.default_rect.y = 6
        self.assertEqual(self.default_rect.y, 6)

        # Test invalid values
        with self.assertRaises(ValueError):
            self.default_rect.width = -1

        with self.assertRaises(TypeError):
            self.default_rect.width = "invalid"

        with self.assertRaises(ValueError):
            self.default_rect.height = 0

        with self.assertRaises(TypeError):
            self.default_rect.x = "invalid"

        with self.assertRaises(ValueError):
            self.default_rect.y = -2

        with self.assertRaises(TypeError):
            self.default_rect.y = "invalid"