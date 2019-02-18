import unittest
from tempconverter import temp_converter

# To run this test, comment out everything except the function in tempconverter.py


class TestTempConverter(unittest.TestCase):
    def test_area(self):
        # Test for real numbers
        self.assertAlmostEqual(temp_converter(65), 18.333333333333332)
        self.assertAlmostEqual(temp_converter(0), -17.77777777777778)
        self.assertAlmostEqual(temp_converter(-2), -18.88888888888889)

    def test_types(self):
        # Raise type errors when necessary
        self.assertRaises(TypeError, temp_converter, 2 + 5j)
        self.assertRaises(TypeError, temp_converter, True)
        self.assertRaises(TypeError, temp_converter, "something")
