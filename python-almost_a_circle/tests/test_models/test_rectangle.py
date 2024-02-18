#!/usr/bin/python3
"""Defines the test cases for 'Rectangle'"""


from models.base import Base
from models.rectangle import Rectangle
import os
import unittest


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class"""
    def test_all_attr_given(self):
        """Test all attributes match what's given"""
        r1 = Rectangle(15, 40, 5, 2, 89)
        self.assertTrue(r1.width == 15)
        self.assertTrue(r1.height == 40)
        self.assertTrue(r1.x == 5)
        self.assertTrue(r1.y == 2)
        self.assertTrue(r1.id == 89)

    def test_zero_height(self):
        """Tests whn the height is zero"""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_rec_area(self):
        """Tests the area of the rectangle"""
        self.assertEqual(Rectangle(4, 5).area(), 20)
        self.assertEqual(Rectangle(2, 3, 0, 0, 7).area(), 6)
        self.assertEqual(Rectangle(8, 20, 3, 4, 76).area(), 160)
        self.assertEqual(Rectangle(4, 7, 2, 1).area(), 28)