import unittest
from task import Number


class TestNumber(unittest.TestCase):

    def test_set_and_get_value(self):
        number = Number(10)
        self.assertEqual(number.get_value(), 10)

        number.set_value(-5)
        self.assertEqual(number.get_value(), -5)

    def test_set_value_type_error(self):
        number = Number()
        with self.assertRaises(TypeError):
            number.set_value(3.14)

    def test_binary_conversion(self):
        number = Number(10)
        self.assertEqual(number.to_binary(), '1010')

        number.set_value(-10)
        self.assertEqual(number.to_binary(), '-1010')

    def test_octal_conversion(self):
        number = Number(8)
        self.assertEqual(number.to_octal(), '10')

        number.set_value(-8)
        self.assertEqual(number.to_octal(), '-10')

    def test_hexadecimal_conversion(self):
        number = Number(255)
        self.assertEqual(number.to_hexadecimal(), 'ff')

        number.set_value(-255)
        self.assertEqual(number.to_hexadecimal(), '-ff')

    def test_special_cases(self):
        special_cases = [
            ("Ноль", 0),
            ("Единица", 1),
            ("Минус единица", -1),
            ("Степень двойки", 256),
            ("Максимум байта", 255),
            ("Степень восьмерки", 512),
            ("Степень шестнадцати", 4096),
            ("Большое число", 1_000_000)
        ]

        for name, value in special_cases:
            with self.subTest(case=name):
                number = Number(value)
                self.assertEqual(number.to_binary(), format(value, 'b'))
                self.assertEqual(number.to_octal(), format(value, 'o'))
                self.assertEqual(number.to_hexadecimal(), format(value, 'x'))


if __name__ == "__main__":
    unittest.main()


