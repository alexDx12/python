"""
1) Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
ноль.
"""


def division():
    """Возвращает результат деления двух чисел."""
    value_1 = float(input("Введите делимое: "))
    value_2 = float(input("Введите делитель: "))
    try:
        result = value_1 / value_2
    except ZeroDivisionError:
        return "Ошибка: деление на 0."
    return f"Результат деления делимого {value_1} на делитель {value_2} равен: {result}."


print(division())
