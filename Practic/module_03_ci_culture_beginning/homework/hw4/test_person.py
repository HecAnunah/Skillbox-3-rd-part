import unittest
from datetime import datetime

from .person import Person


class TestPerson(unittest.TestCase):
    def test_get_name(self):
        p = Person("Ivan", 2000)
        self.assertEqual(p.get_name(), "Ivan")

    def test_set_name(self):
        p = Person("Ivan", 2000)
        p.set_name("Petr")
        self.assertEqual(p.get_name(), "Petr")

    def test_get_age(self):
        p = Person("Ivan", 2000)
        current_year = datetime.now().year
        expected_age = current_year - 2000
        self.assertEqual(p.get_age(), expected_age)

    def test_get_address(self):
        p = Person("Ivan", 2000, "Moscow")
        self.assertEqual(p.get_address(), "Moscow")

    def test_set_address(self):
        p = Person("Ivan", 2000)
        p.set_address("Saint-Petersburg")
        self.assertEqual(p.get_address(), "Saint-Petersburg")

    def test_is_homeless_true(self):
        p = Person("Ivan", 2000)
        self.assertTrue(p.is_homeless())

    def test_is_homeless_false(self):
        p = Person("Ivan", 2000, "Ekaterinburg")
        self.assertFalse(p.is_homeless())
