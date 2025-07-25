import unittest
from block_errors import BlockErrors


class TestBlockErr(unittest.TestCase):
    def test_suppress_specified_exception(self):
        try:
            with BlockErrors(ValueError):
                raise ValueError("ignore me")
        except ValueError:
            self.fail("ValueError не должен был проброшен")

    def test_do_not_other_exc(self):
        with self.assertRaises(TypeError):
            with BlockErrors(ValueError):
                raise TypeError("should not be suppressed")

    def test_multiple_exc(self):
        try:
            with BlockErrors(ValueError, KeyError):
                raise KeyError("also ignored")
        except Exception:
            self.fail("KeyError не должен был проброшен")

    def test_no_exc(self):
        try:
            with BlockErrors(ValueError):
                x = 1 + 1 
        except Exception:
            self.fail("Никакие исключения не должны были быть") 




if __name__ == '__main__':
    unittest.main()