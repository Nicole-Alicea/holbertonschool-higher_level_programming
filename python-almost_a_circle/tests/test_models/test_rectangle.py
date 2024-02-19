#!/usr/bin/python3
"""Defines the test cases for 'Rectangle'"""


import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys


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

    def test_area(self):
        """Test the area calculation"""
        self.assertEqual(self.default_rect.area(), 2 * 4)

    def test_display(self):
        """Test the display method"""
        # Redirect stdout to capture the printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        self.default_rect.display()

        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Get the printed output
        printed_output = captured_output.getvalue()

        # Adjust the expected output to include leading spaces
        expected_output = "  ##\n  ##\n  ##\n  ##\n"
        self.assertEqual(printed_output, expected_output)

    def test_str(self):
        """Test the __str__ method"""
        expected_str = "[Rectangle] (1) 0/0 - 2/4"
        self.assertEqual(str(self.default_rect), expected_str)

    def test_update(self):
        """Test the update method"""
        self.default_rect.update(2, 3, 5, 1, 2)
        self.assertEqual(self.default_rect.id, 2)
        self.assertEqual(self.default_rect.width, 3)
        self.assertEqual(self.default_rect.height, 5)
        self.assertEqual(self.default_rect.x, 1)
        self.assertEqual(self.default_rect.y, 2)

    def test_to_dictionary(self):
        """Test the to_dictionary method"""
        expected_dict = {'id': 1, 'width': 2, 'height': 4, 'x': 0, 'y': 0}
        self.assertEqual(self.default_rect.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()