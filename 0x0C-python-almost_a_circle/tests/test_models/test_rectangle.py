#!/usr/bin/python3
"""Test base module."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test Base class.
    """
    def test_create_rectangle(self):   # Task 2: create class Rectangle
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.id, 6)   # previous id stopped at 5

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.id, 7)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r3.id, 12)

        # When less than 2 args are supplied
        with self.assertRaises(TypeError):
            r4 = Rectangle()
        with self.assertRaises(TypeError):
            r4 = Rectangle(10)

        # When more than 5 args are supplied
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, 2, 0, 0, 100, 1)

    def test_validate_rectangle(self):
        # Task 3: update class Rectangle (implement validation)

        # Test `width`, `height`, `x` and `y` validators respectively.
        # --------------------> TypeErrors <-------------------
        # check string assignment
        with self.assertRaises(TypeError):
            r5 = Rectangle('a string', 2, 0)
        with self.assertRaises(TypeError):
            r5 = Rectangle(1, 'another string', 1)
        with self.assertRaises(TypeError):
            r5 = Rectangle(1, 1, 'yet another string')
        with self.assertRaises(TypeError):
            r5 = Rectangle(1, 3, 0, 'even one more string')

        # check others
        r5 = Rectangle(1, 3, 4, 5)
        with self.assertRaises(TypeError):
            r5.width = [1, 2, 3, 4, 5]
        with self.assertRaises(TypeError):
            r5.height = (321, 13)
        with self.assertRaises(TypeError):
            r5.x = {'1': 2, '2': 3, '3': 4}
        with self.assertRaises(TypeError):
            r5.y = 13212.4

        # --------------------> ValueErrors <-------------------
        with self.assertRaises(ValueError):  # width must be > 0
            r6 = Rectangle(0, 1)
        with self.assertRaises(ValueError):  # height must be > 0
            r6 = Rectangle(5, 0)
        with self.assertRaises(ValueError):  # x must be >= 0
            r6 = Rectangle(5, 1, -1)
        with self.assertRaises(ValueError):  # y must be >= 0
            r6 = Rectangle(5, 1, 0, -1)
        # ckeck others
        r6 = Rectangle(1, 3)
        with self.assertRaises(ValueError):  # width must be > 0
            r6.width = 0
        with self.assertRaises(ValueError):  # width must be > 0
            r6.width = -1
        with self.assertRaises(ValueError):  # height must be > 0
            r6.height = 0
        with self.assertRaises(ValueError):  # height must be > 0
            r6.height = -132
        with self.assertRaises(ValueError):  # x must be >= 0
            r6.x = -1
        with self.assertRaises(ValueError):  # y must be >= 0
            r6.y = -123

    def test_area(self):         # Task 4:
        r7 = Rectangle(10, 2, 1, 1, 32)
        self.assertEqual(r7.area(), 20)
        r8 = Rectangle(2, 4, 1, 1, 32)
        self.assertEqual(r8.area(), 8)
        r8.width = 1
        self.assertEqual(r8.area(), 4)
        r8.width = 2
        r8.height = 3
        self.assertEqual(r8.area(), 6)

        # Calling `area()` method with args should raise exception.
        with self.assertRaises(TypeError):
            r8.area(2)
        with self.assertRaises(TypeError):
            r8.area(2, 3, 4)

    def test_display(self):      # Task 5:
        # calling `dispay()` method with args should raise exception.
        r9 = Rectangle(4, 5, 0, 0, 12)
        with self.assertRaises(TypeError):
            r9.display(1)
        with self.assertRaises(TypeError):
            r9.display(1, 3, 6)

        # if height, width, x or y is a very large integer memory error is
        # raised.
        with self.assertRaises(OverflowError):
            r9.width = 10000000000000000000  # Exactly 20 digits
            r9.display()
        with self.assertRaises(MemoryError):
            r9.width = 10000000000  # Exactly 11 digits
            r9.display()
        r9.width = 4  # re-assign 4 back to `width` for other tests

        with self.assertRaises(OverflowError):
            r9.x = 10000000000000000000
            r9.display()
        with self.assertRaises(MemoryError):
            r9.x = 10000000000
            r9.display()
        r9.x = 0  # re-assign 0 back to `x` for other tests

        with self.assertRaises(OverflowError):
            r9.y = 10000000000000000000
            r9.display()
        with self.assertRaises(MemoryError):
            r9.y = 10000000000
            r9.display()
        r9.y = 0  # re-assign 0 back to `y` for other tests

    # Skipped Task 6(`__str__()` method)
    # Skipped Task 7(update `display()` method)

    def test_update_1(self):   # Task 8: create
        r10 = Rectangle(1, 1, 0, 0, 100)
        args = (12, 10, 5, 1, 1)

        # try passing complete args
        r10.update(*args)
        self.assertEqual(r10.id, 12)
        self.assertEqual(r10.width, 10)
        self.assertEqual(r10.height, 5)
        self.assertEqual(r10.x, 1)
        self.assertEqual(r10.y, 1)

        # try passing empty *args
        r11 = Rectangle(1, 1, 0, 0, 101)
        args = ()
        r11.update(*args)
        self.assertEqual(r11.id, 101)
        self.assertEqual(r11.width, 1)
        self.assertEqual(r11.height, 1)
        self.assertEqual(r11.x, 0)
        self.assertEqual(r11.y, 0)

        # try passing some *args
        r11 = Rectangle(1, 1, 0, 0, 101)
        args = (1, 2, 3)
        r11.update(*args)
        self.assertEqual(r11.id, 1)
        self.assertEqual(r11.width, 2)
        self.assertEqual(r11.height, 3)
        self.assertEqual(r11.x, 0)
        self.assertEqual(r11.y, 0)

        # When args contains too much arguments (greater than 5), only
        # values of index zero to four are used
        args = (12, 10, 5, 1, 1, 21, 23, 43)
        r11.update(*args)
        self.assertEqual(r11.id, 12)
        self.assertEqual(r11.width, 10)
        self.assertEqual(r11.height, 5)
        self.assertEqual(r11.x, 1)
        self.assertEqual(r11.y, 1)

    def test_update_2(self):   # Task 9: Update
        pass
