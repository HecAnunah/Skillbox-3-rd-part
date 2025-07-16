import unittest
import os
import random
from previous_hw_test.head_file import app

FILENAME = "new_file.txt"
BINFILE = "new_binfile.bin"


class TestSum(unittest.TestCase):
    def setUp(self) -> None:
        app.config["TESTING"] = True
        self.client = app.test_client()

        with open(FILENAME, "w", encoding="utf-8") as f:
            f.write("Hellow my new lesson. I create a new file.")

        with open(BINFILE, "wb") as f2:
            file_size = 1024
            rd_data = bytearray(random.getrandbits(8) for _ in range(file_size))
            f2.write(rd_data)

    def tearDown(self) -> None:
        for file_name in (FILENAME, BINFILE):
            if os.path.exists(file_name):
                os.remove(file_name)

    def test_exist_file(self):
        response = self.client.get(f"/head/{FILENAME}")
        self.assertEqual(response.status_code, 200)

    def test_file_text(self):
        response = self.client.get(f"/head/{FILENAME}")
        self.assertIn("Hellow", response.data.decode())

    def test_none_file(self):
        response = self.client.get(f"/head/not_real_file.txt")
        self.assertEqual(response.status_code, 404)

    def test_empty_file(self):
        empty_file = "empty_file.txt"
        with open(empty_file, "w", encoding="utf-8") as f:
            pass
        response = self.client.get(f"/head/{empty_file}")
        self.assertEqual(response.status_code, 400)

        os.remove(empty_file)

    def test_bin_file(self):
        response = self.client.get(f"/head/{BINFILE}")
        self.assertEqual(response.status_code, 400)
