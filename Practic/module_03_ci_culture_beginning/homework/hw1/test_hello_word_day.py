import unittest
from .hello_word_with_day import app, GREETINGS
from datetime import datetime
from freezegun import freeze_time


class TestHelloWord(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        self.client = app.test_client()
        self.base_url = "/hello-world"

    def chek_datetime(self, freeze_date: str, expected_greeting: str):
        name = "username"

        with freeze_time(freeze_date):
            urls = self.base_url + "/" + name
            response = self.client.get(urls)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                response.data.decode("utf-8"), f"Привет, {name}. {expected_greeting}!"
            )

    def test_date_1(self):
        self.chek_datetime("2024-07-15", GREETINGS[0])

    def test_date_2(self):
        self.chek_datetime("2024-07-16", GREETINGS[1])

    def test_date_3(self):
        self.chek_datetime("2024-07-17", GREETINGS[2])

    def test_date_4(self):
        self.chek_datetime("2024-07-18", GREETINGS[3])

    def test_date_5(self):
        self.chek_datetime("2024-07-19", GREETINGS[4])

    def test_date_6(self):
        self.chek_datetime("2024-07-20", GREETINGS[5])

    def test_date_7(self):
        self.chek_datetime("2024-07-21", GREETINGS[6])

    def test_username(self):
        name = "Хорошего дня"
        urls = self.base_url + "/" + name
        response = self.client.get(urls)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode("utf-8"), "Имя должно быть односоставным")
