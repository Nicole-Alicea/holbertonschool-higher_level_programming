#!/usr/bin/python3
"""Test cases for 'Base' class"""


import unittest
import os
import json
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    '''Tests for base.py'''
    def setUp(self) -> None:
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_id_auto(self):
        '''Tests the assigment of id automatically'''
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(15)
        b5 = Base()
        self.assertTrue(b1, self.id == 1)
        self.assertTrue(b2, self.id == 2)
        self.assertTrue(b3, self.id == 3)
        self.assertTrue(b4, self.id == 15)
        self.assertTrue(b5, self.id == 4)

    def test_id_given(self):
        """Tests the matching of id given"""
        self.assertTrue(Base(200), self.id == 200)
        self.assertTrue(Base(-5), self.id == -5)
        self.assertTrue(Base(91432), self.id == 91432)
        self.assertTrue(Base(0), self.id == 0)

    def test_id_is_none(self):
        """Test id is none
        """
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)
        self.assertTrue(Base(), self.id == 3)

    def test_1_id(self):
        """After run set of ids"""
        Base._Base__nb_objects = 0
        bas = Base()
        self.assertEqual(bas.id, 1)
        t1 = Base(25)
        self.assertEqual(t1.id, 25)
        t2 = Base(-45)
        self.assertEqual(t2.id, -45)
        t3 = Base()
        self.assertEqual(t3.id, 2)

    def test_private_att_access(self):
        """Tests access of private attribute"""
        with self.assertRaises(AttributeError):
            Base.__nb_objects
            Base.nb_objects
            Base._nb_objects

    def test_invalid_args(self):
        """Tests more than one args given"""
        with self.assertRaises(TypeError):
            Base(55, 15)

    def test_attribute_error(self):
        """Tests when accessing prvate class attr"""
        b = Base(67)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)

    def test_class(self):
        '''Test if the class is Base'''
        self.assertTrue(Base(2), self.__class__ == Base)

    def test_create(self):
        """Tests whether create returns an
        instance with all attributes already set
        """
        rectangle1 = Rectangle(2, 3, 4, 5, 9)
        dic = rectangle1.to_dictionary()
        rectangle2 = Rectangle.create(**dic)
        self.assertEqual(str(rectangle1), '[Rectangle] (9) 4/5 - 2/3')
        self.assertEqual(str(rectangle2), '[Rectangle] (9) 4/5 - 2/3')
        self.assertIsNot(rectangle1, rectangle2)

    def test_from_json_string_type(self):
        list_input = [{"id": 36, "width": 15, "height": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_none_load_from_file(self):
        Rectangle.save_to_file(None)
        recs = Rectangle.load_from_file()
        self.assertEqual(type(recs), list)
        self.assertEqual(len(recs), 0)

if __name__ == "__main__":
    unittest.main()