from materials.flask_wtform import app, RegistrationForm

import unittest
import re


class TestWtform(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["TESTING"] = True
        cls.client = app.test_client()
        cls.base_url = "/registration"

    def make_request(self, exc_field: str = ''):
        form_data = {
            "email": "test@example.com",
            "phone": "9991234567",
            "name": "Иванов И.И.",
            "address": "улица Пушкина",
            "index": "123456",
            "comment": "тест",
        }

        form_data.pop(exc_field)  # delete Key and value for test_**
        response = self.client.post(self.base_url, data=form_data)

        return response

    def test_name(self):
        response = self.make_request("name")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"name", response.data)

    def test_correct_name_imput(self):
        valid_name = ["Захар П.В.", "Захар О.А."]
        invalid_name = ["Зак", "Антон"]
        for n in valid_name:
            with self.subTest(name=n):
                response = self.client.post(
                    self.base_url,
                    data={
                        "email": "test@example.com",
                        "phone": "9991234567",
                        "name": n,
                        "address": "ул. Ленина",
                    },
                )
                self.assertEqual(response.status_code, 200)

        for n in invalid_name:
            with self.subTest(name=n):
                response = self.client.post(
                    self.base_url,
                    data={
                        "email": "test@example.com",
                        "phone": "9991234567",
                        "name": n,
                        "address": "ул. Ленина",
                    },
                )
                self.assertEqual(response.status_code, 400)

    def test_email(self):
        response = self.make_request("email")

        self.assertEqual(response.status_code, 400)
        self.assertIn(b"email", response.data)

    def test_phone(self):
        response = self.make_request("phone")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"phone", response.data)

    def test_len_phone(self):
        valid_phone = "9991234567"
        invalid_phone = ["12132", "321312", "231234444"]
        response = self.client.post(
            self.base_url,
            data={
                "email": "test@example.com",
                "phone": valid_phone,
                "name": "Захар О.А.",
                "address": "ул. Ленина",
            },
        )
        self.assertTrue(response.status_code, 200)

        for phone in invalid_phone:
            with self.subTest(ph_number=phone):
                response = self.client.post(
                    self.base_url,
                    data={
                        "email": "test@example.com",
                        "phone": phone,
                        "name": "Захар О.А.",
                        "address": "ул. Ленина",
                    },
                )
                self.assertEqual(response.status_code, 400)
                self.assertIn(b"phone", response.data)

    def test_address(self):
        response = self.make_request("address")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"address", response.data)
