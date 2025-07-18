import unittest
from .accounting import app, storage
from datetime import datetime


class TestAccaunting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        storage.clear()
        cls.sample_data = {
            2024: {
                7: {
                    18: 100,
                    19: 200,
                },
                "total": 300,
            },
            2025: {
                1: {1: 50},
                "total": 50,
            },
        }
        storage.update(cls.sample_data)

    def setUp(self) -> None:
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        self.client = app.test_client()

    # add test
    def test_add_valid_date(self):
        numb = 500

        response = self.client.get(f"add/20250717/{numb}")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Добавлено 500 руб", response.data.decode())

    def test_add_invalid_date(self):
        response = self.client.get("/add/20252025/1234")
        self.assertEqual(response.status_code, 400)
        self.assertIn("Некорректная дата", response.data.decode())

    # calculate/<year> test

    def test_calculate_year_existing(self):
        response = self.client.get("/calculate/2024")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Добавлено 300 руб. за 2024 год", response.data.decode())

    def test_calculate_year_not_in_data(self):
        response = self.client.get("/calculate/2020")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Нет данных за 2020 год", response.data.decode())

    # /calculate/<year>/<month> test

    def test_calculate_month_existing(self):
        response = self.client.get("/calculate/2024/7")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Суммарные траты", response.data.decode())
        self.assertIn("300", response.data.decode())  # total за год
        self.assertIn("300", response.data.decode())  # сумма по месяцу

    def test_calculate_month_no_month(self):
        response = self.client.get("/calculate/2024/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Нет данных за 1 месяц", response.data.decode())

    def test_calculate_month_no_year(self):
        response = self.client.get("/calculate/2019/5")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Нет данных за 2019 год", response.data.decode())

    # Пустой storage

    def test_calculate_with_empty_storage(self):
        storage.clear()
        response_year = self.client.get("/calculate/2024")
        self.assertIn("Нет данных за 2024 год", response_year.data.decode())

        response_month = self.client.get("/calculate/2024/7")
        self.assertIn("Нет данных за 2024 год", response_month.data.decode())
