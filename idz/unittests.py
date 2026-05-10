import unittest

from main import check_is_even


class TestIsEven(unittest.TestCase):
    def test_even_numbers(self):
        self.assertTrue(check_is_even("2"))
        self.assertTrue(check_is_even("0"))
        self.assertTrue(check_is_even("-100"))

    def test_odd_numbers(self):
        self.assertFalse(check_is_even("3"))
        self.assertFalse(check_is_even("-7"))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            check_is_even("текст")

        with self.assertRaises(ValueError):
            check_is_even("3.14")

        with self.assertRaises(ValueError):
            check_is_even("")


if __name__ == "__main__":
    unittest.main()
