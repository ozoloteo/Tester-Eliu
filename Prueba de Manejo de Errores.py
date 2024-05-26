# error_handling.py
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

# test_error_handling.py
import unittest
from error_handling import divide

class TestErrorHandling(unittest.TestCase):

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(1, 0)

    def test_divide_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5)

if __name__ == '__main__':
    unittest.main()
