"""
Для каждого поля и валидатора в эндпоинте /registration напишите юнит-тест,
который проверит корректность работы валидатора. Таким образом, нужно проверить, что существуют наборы данных,
которые проходят валидацию, и такие, которые валидацию не проходят.
"""

import unittest
from Practic.module_04_flask.homework.hw1_3.hw1_registration import app


class TestValidation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["TESTING"] = True
        cls.client = app.test_client()
        cls.base_url = "/registration"

    def make_request(self, exc_field: str):
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
        valid_name = ["Ант П.В.", "Ольга О.А."]
        invalid_name = ["Дмитрий", "Антон"]
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


if __name__ == "__main__":
    unittest.main()
