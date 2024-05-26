# person.py
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_adult(self):
        return self.age >= 18

# test_person.py
import unittest
from person import Person

class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person = Person('John', 'Doe', 25)

    def test_full_name(self):
        self.assertEqual(self.person.full_name(), 'John Doe')

    def test_is_adult(self):
        self.assertTrue(self.person.is_adult())

    def test_is_not_adult(self):
        self.person.age = 15
        self.assertFalse(self.person.is_adult())

if __name__ == '__main__':
    unittest.main()
