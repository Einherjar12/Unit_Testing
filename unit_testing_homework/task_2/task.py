# Задание 2
# Создайте класс для числа. В классе должна быть реализована следующая функциональность:
# ■ Запись и чтение значения.
# ■ Перевод числа в восьмеричную систему исчисления.
# ■ Перевод числа в шестнадцатеричную систему исчисления.
# ■ Перевод числа в двоичную систему исчисления.
# Протестируйте все возможности созданного класса
# с помощью модульного тестирования(unittest).

class Number:
    """
    Класс для работы с целым числом.
    """

    def __init__(self, value=0):
        self.set_value(value)

    def set_value(self, value):
        if not isinstance(value, int):
            raise TypeError("Значение должно быть целым числом")
        self._value = value

    def get_value(self):
        return self._value

    def to_binary(self):
        return format(self._value, 'b')

    def to_octal(self):
        return format(self._value, 'o')

    def to_hexadecimal(self):
        return format(self._value, 'x')

