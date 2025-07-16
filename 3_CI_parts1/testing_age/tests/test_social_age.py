import unittest

from social_age import get_social_status


class TestSocialAge(unittest.TestCase):
    def test_can_get_child_age_13(self):
        age = 8
        expected_res = "ребенок"
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)


    def test_can_get_child_age_18(self):
        age = 15
        expected_res = "подросток"
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)

    def test_can_get_child_age_50(self):
        age = 45
        expected_res = "взрослый"
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)

    def test_can_get_child_age_65(self):
        age = 60
        expected_res = "пожилой"
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)


    # Негативный тест. Пройден - если поймал ошибку.
    def test_cannot_pass_str_as_age(self):
        age = '+'
        with self.assertRaises(ValueError):
            get_social_status(age)