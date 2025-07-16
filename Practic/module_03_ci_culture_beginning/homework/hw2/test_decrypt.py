import unittest
import sys
import io

from .decrypt import decrypt


class TestDecrypt(unittest.TestCase):
    def setUp(self):
        self.test = [
            ("абра-кадабра.", "абра-кадабра"),
            ("абраа..-кадабра", "абра-кадабра"),
            ("абраа..-.кадабра", "абра-кадабра"),
            ("абра--..кадабра", "абра-кадабра"),
            ("абрау...-кадабра", "абра-кадабра"),
            ("абра........", ""),
            ("абр......a.", "a"),
            ("1..2.3", "23"),
            (".", ""),
            ("1.......................", ""),
        ]

    def tearDown(self) -> None:
        sys.stdin = sys.__stdin__

    def test_decrypto(self) -> None:
        for encrypto, expected in self.test:
            with self.subTest(encrypto=encrypto):
                self.assertEqual(decrypt(encrypto), expected)

    def test_stdin(self) -> None:
        for encrypto, expected in self.test:
            with self.subTest(encrypto=encrypto):
                sys.stdin = io.StringIO(encrypto)
                data = sys.stdin.read()
                self.assertEqual(decrypt(data), expected)
