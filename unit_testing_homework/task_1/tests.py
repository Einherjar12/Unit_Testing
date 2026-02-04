import unittest
from task import NumbersSet


class TestNumbersSet(unittest.TestCase):

    def setUp(self):
        self.positive = NumbersSet([1, 2, 3, 4, 5])
        self.negative = NumbersSet([-1, -2, -3, -4])
        self.mixed = NumbersSet([-10, 0, 10, 20])
        self.single = NumbersSet([7])
        self.empty = NumbersSet()

    # ---------- Положительные числа ----------

    def test_positive_sum(self):
        self.assertEqual(self.positive.get_sum(), 15)

    def test_positive_average(self):
        self.assertEqual(self.positive.get_average(), 3)

    def test_positive_max(self):
        self.assertEqual(self.positive.get_max(), 5)

    def test_positive_min(self):
        self.assertEqual(self.positive.get_min(), 1)

    # ---------- Отрицательные числа ----------

    def test_negative_sum(self):
        self.assertEqual(self.negative.get_sum(), -10)

    def test_negative_average(self):
        self.assertEqual(self.negative.get_average(), -2.5)

    def test_negative_max(self):
        self.assertEqual(self.negative.get_max(), -1)

    def test_negative_min(self):
        self.assertEqual(self.negative.get_min(), -4)

    # ---------- Смешанные числа ----------

    def test_mixed_sum(self):
        self.assertEqual(self.mixed.get_sum(), 20)

    def test_mixed_average(self):
        self.assertEqual(self.mixed.get_average(), 5)

    def test_mixed_max(self):
        self.assertEqual(self.mixed.get_max(), 20)

    def test_mixed_min(self):
        self.assertEqual(self.mixed.get_min(), -10)

    # ---------- Один элемент ----------

    def test_single_values(self):
        self.assertEqual(self.single.get_sum(), 7)
        self.assertEqual(self.single.get_average(), 7)
        self.assertEqual(self.single.get_max(), 7)
        self.assertEqual(self.single.get_min(), 7)

    # ---------- Пустой набор ----------

    def test_empty_set(self):
        self.assertEqual(self.empty.get_sum(), 0)
        self.assertEqual(self.empty.get_average(), 0)
        self.assertIsNone(self.empty.get_max())
        self.assertIsNone(self.empty.get_min())

    # ---------- Валидация ----------

    def test_input_validation(self):
        """Тест валидации входных данных."""

        # Некорректные данные при инициализации
        with self.assertRaises(ValueError):
            NumbersSet([1, 2, "3"])

        with self.assertRaises(ValueError):
            NumbersSet([1.5, 2, 3])

        # Некорректные данные при добавлении
        with self.assertRaises(ValueError):
            self.empty.add_number("not a number")

        with self.assertRaises(ValueError):
            self.empty.add_number(3.14)


if __name__ == "__main__":
    unittest.main()

