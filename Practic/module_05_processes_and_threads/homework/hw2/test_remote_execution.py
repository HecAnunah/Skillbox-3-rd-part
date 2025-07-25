import unittest
from reomote_exe import app


class TestRemote(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["TESTING"] = True
        cls.client = app.test_client()
        cls.base_url = "/run_code"

    def test_commands_true(self):
        data = {"code": "for i in range(3): print(i)", "timeout": 2}
        response = self.client.post(
            self.base_url, data=data, content_type="application/x-www-form-urlencoded"
        )
        self.assertEqual(response.status_code, 200)

        resp_decode = response.data.decode().strip()
        self.assertEqual(resp_decode, "0\n1\n2")

    def test_timeout(self):
        data = {"code": "import time; time.sleep(5)", "timeout": 1}
        response = self.client.post(
            self.base_url, data=data, content_type="application/x-www-form-urlencoded"
        )
        self.assertEqual(
            "Ошибка: время выполнения кода истякло.", response.data.decode()
        )

    def test_invalid_data(self):
        data = {"code": "", "timeout": 0}
        response = self.client.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 400)

    def test_dungerous(self):
        data = {"code": "import os; os.system('echo hacked')", "timeout": 1}
        response = self.client.post(
            self.base_url, data=data, content_type="application/x-www-form-urlencoded"
        )

        self.assertNotIn("hacked", response.data.decode())


if __name__ == "__main__":
    unittest.main()
