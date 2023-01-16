#!/usr/bin/python3
"""Test base module."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test Base class.
    """
    def test_priv_attr(self):      # Test task 1
        with self.assertRaises(AttributeError):
            print(self.nb_objects)
            print(self.__nb_objects)

    def test___init__(self):       # Test task 1
        b1 = Base()  # create 1st base object
        self.assertEqual(b1.id, 1)
        b2 = Base()  # create 2nd base object
        self.assertEqual(b2.id, 2)
        b3 = Base()  # create 3rd base object
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)
        b6 = Base(None)
        self.assertEqual(b6.id, 5)  # default id should be 5

        # When non-integer values is assigned
        b7 = Base('Alex')              # string
        self.assertEqual(b7.id, 'Alex')
        b8 = Base([])                  # list
        self.assertEqual(b8.id, [])
        b9 = Base([1, 2, 3])           # list
        self.assertEqual(b9.id, [1, 2, 3])
        b10 = Base(())                 # tuple
        self.assertEqual(b10.id, ())
        b11 = Base(1.123213)           # float
        self.assertEqual(b11.id, 1.123213)

        # When more than one argument is supplied
        with self.assertRaises(TypeError):
            b12 = Base(123, 2)
            b13 = Base('adfasd', 13312)
