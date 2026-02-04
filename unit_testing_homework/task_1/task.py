# Задание 1. Создайте класс, содержащий набор целых чисел.
# В классе должна быть реализована следующая функциональность:
# ■ Сумма элементов набора.
# ■ Среднеарифметическое элементов набора.
# ■ Максимум из элементов набора.
# ■ Минимум из элементов набора.
# Протестируйте все возможности созданного класса
# с помощью модульного тестирования(unittest).

class NumbersSet:
    """
    Класс для работы с набором целых чисел.
    """

    def __init__(self, numbers=None):
        """
        Инициализация набора чисел.

        """
        self.numbers = []

        if numbers is not None:
            if not isinstance(numbers, list):
                raise ValueError("numbers должен быть списком")

            for number in numbers:
                self._validate_number(number)
                self.numbers.append(number)

    def _validate_number(self, number):
        """Проверка, что значение является целым числом"""
        if not isinstance(number, int):
            raise ValueError("Допускаются только целые числа")

    def add_number(self, number):
        """Добавляет число в набор"""
        self._validate_number(number)
        self.numbers.append(number)

    def get_sum(self):
        """Возвращает сумму элементов набора"""
        return sum(self.numbers)

    def get_average(self):
        """Возвращает среднее арифметическое элементов набора"""
        if not self.numbers:
            return 0
        return sum(self.numbers) / len(self.numbers)

    def get_max(self):
        """Возвращает максимальный элемент набора"""
        if not self.numbers:
            return None
        return max(self.numbers)

    def get_min(self):
        """Возвращает минимальный элемент набора"""
        if not self.numbers:
            return None
        return min(self.numbers)
