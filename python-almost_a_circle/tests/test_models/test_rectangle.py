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