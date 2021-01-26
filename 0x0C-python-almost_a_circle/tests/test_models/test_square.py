#!/usr/bin/python3
"""
Test for the Square class
"""

import unittest
import json
from models import square
from models.base import Base
Square = square.Square


class TestSquare(unittest.TestCase):
    """Test the functionality of the Square class"""
    @classmethod
    def setUpClass(cls):
        """set up the tests"""
        Base._Base__nb_objects = 0
        cls.s1 = Square(1)
        cls.s2 = Square(2, 3)

    def test_id(self):
        """Test for functioning ID"""
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)

    def test_size(self):
        """Test for functioning size"""
        self.assertEqual(self.s1.size, 1)
        self.assertEqual(self.s2.size, 2)

    def test_width(self):
        self.assertEqual(self.s1.width, 1)
        self.assertEqual(self.s2.width, 2)

    def test_height(self):
        """Test for functioning height"""
        self.assertEqual(self.s1.height, 1)
        self.assertEqual(self.s2.height, 2)

    def test_x(self):
        """Test for functioning x"""
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 3)

    def test_y(self):
        """Test for functioning y"""
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 0)

    def mandatory_size(self):
        """Test that width is a mandatory arg"""
        with self.assertRaises(TypeError):
            s = Square()

    def size_typeerror(self):
        """Test non-ints for size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("hello")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(True)

    def test_x_typeerror(self):
        """Test non-ints for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, True)

    def test_y_typeerror(self):
        """Test non-ints for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 1, True)

    def test_size_valueerror(self):
        """Test ints <= 0 for size"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0)

    def test_x_valueerror(self):
        """Test ints < 0 for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s = Square(1, -1)

    def test_y_valueerror(self):
        """Test ints <= 0 for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s = Square(1, 1, -1)

    def test_area(self):
        """test area"""
        self.assertEqual(self.s1.area(), 1)
        self.assertEqual(self.s2.area(), 4)

    def test_area_args(self):
        """Test too many args for area()"""
        with self.assertRaises(TypeError):
            a = self.s1.area(1)

    def test_display_too_many_args(self):
        """Test display with too many args"""
        with self.assertRaises(TypeError):
            self.s1.display(1)
