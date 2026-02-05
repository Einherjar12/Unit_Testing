from task import Number

cases = [
    ("Ноль", 0),
    ("Единица", 1),
    ("Минус единица", -1),
    ("Положительное число", 42),
    ("Отрицательное число", -42),
    ("Степень двойки", 256),
    ("Максимум байта", 255),
    ("Степень восьмерки", 512),
    ("Степень шестнадцати", 4096),
    ("Большое число", 1_000_000)
]

print("Демонстрация работы класса Number:\n")

for name, value in cases:
    number = Number(value)
    print(f"{name}:")
    print(f"  Значение: {number.get_value()}")
    print(f"  Двоичная система: {number.to_binary()}")
    print(f"  Восьмеричная система: {number.to_octal()}")
    print(f"  Шестнадцатеричная система: {number.to_hexadecimal()}")
    print("-" * 40)


