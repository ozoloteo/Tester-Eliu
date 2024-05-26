# string_functions.py
def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

# test_string_functions.py
import unittest
from string_functions import reverse_string, is_palindrome

class TestStringFunctions(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string('hello'), 'olleh')

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('madam'))
        self.assertFalse(is_palindrome('hello'))

if __name__ == '__main__':
    unittest.main()
