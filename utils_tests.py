import unittest
from utils import utils


class TestUtils(unittest.TestCase):

    ###### Tests for reversed() #####

    def test_reversed_integer(self):
        self.assertEqual(utils.reversed(123), 321)
        self.assertEqual(utils.reversed(-456), -654)
        self.assertEqual(utils.reversed(100), 1)

    def test_reversed_string_raises_error(self):
        with self.assertRaises(TypeError):
            utils.reversed("123")

    def test_reversed_float_raises_error(self):
        with self.assertRaises(TypeError):
            utils.reversed(123.45)

    ###### Tests for formatter() #####

    def test_formatter_integer(self):
        binary, octal = utils.formatter(8)
        self.assertEqual(binary, "0b1000")
        self.assertEqual(octal, "0o10")

    def test_formatter_string_raises_error(self):
        with self.assertRaises(TypeError):
            utils.formatter("8")

    def test_formatter_float_raises_error(self):
        with self.assertRaises(TypeError):
            utils.formatter(8.5)


if __name__ == "__main__":
    unittest.main()