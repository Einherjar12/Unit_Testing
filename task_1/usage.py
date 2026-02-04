from task import NumbersSet


class NumbersSetDemo:
    """Класс для демонстрации работы NumbersSet"""
    @staticmethod
    def show_example(title, numbers_set):
        print(f"\n{title}")
        print("Числа:", numbers_set.numbers)
        print("Сумма:", numbers_set.get_sum())
        print("Среднее:", numbers_set.get_average())
        print("Максимум:", numbers_set.get_max())
        print("Минимум:", numbers_set.get_min())


if __name__ == "__main__":

    # Пример 1: положительные числа
    positive = NumbersSet([1, 2, 3, 4, 5])
    NumbersSetDemo.show_example("Пример 1: Положительные числа", positive)

    # Пример 2: смешанные числа
    mixed = NumbersSet([-10, 0, 10, 20])
    NumbersSetDemo.show_example("Пример 2: Смешанные числа", mixed)

    # Пример 3: пустой набор
    empty = NumbersSet()
    NumbersSetDemo.show_example("Пример 3: Пустой набор", empty)

