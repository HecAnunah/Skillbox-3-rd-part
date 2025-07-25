import unittest
from redirect import Redirect
import io
import sys


class TestRedirect(unittest.TestCase):
    def setUp(self):
        self.fake_io = io.StringIO()

    def test_out(self):
        with Redirect(stdout=self.fake_io):
            print("Hellow world")
        self.assertIn("Hellow world", self.fake_io.getvalue())

    def test_err(self):
        try:
            with Redirect(stderr=self.fake_io):
                raise ValueError("Test Error")
        except Exception:
            pass

        value = self.fake_io.getvalue()
        self.assertIn("ValueError", value)
        self.assertIn("Test Error", value)

    def test_duble_stream(self):
        fake_stdout = io.StringIO()
        fake_stderr = io.StringIO()
        with Redirect(stderr=fake_stderr, stdout=fake_stdout):
            print("Go in stdOut")
            sys.stderr.write("Go in stdErr")

        self.assertIn("Go in stdOut", fake_stdout.getvalue())
        self.assertIn("Go in stdErr", fake_stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
