"""
5) Реализовать формирование списка, используя функцию range() и возможности генератора. В
список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить
результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce() .
"""

from functools import reduce


def multiplication(el, next_el):
    """Умножает текущий элемент на следующий в списке."""
    return el * next_el


actual_list = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(multiplication, actual_list))
