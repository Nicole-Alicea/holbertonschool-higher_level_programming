#!/usr/bin/python3
"""Defines tests for 'Square' class"""


import unittest
from models.square import Square

class TestSquareMethods(unittest.TestCase):

    def setUp(self):
        """Set up a default Square instance for testing"""
        self.default_square = Square(size=3, id=1)
