# math_functions.py
def add(a, b):
    return a + b

# test_math_functions.py
import unittest
from math_functions import add

class TestMathFunctions(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
