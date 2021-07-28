#5. Реализовать формирование списка, используя функцию range()
# и возможности генератора.
# В список должны войти четные числа  от 100 до 1000 (включая границы).
# Необходимо получить результат  вычисления произведения всех элементов списка.

# одсказка: использовать функцию reduce().
from functools import reduce

def multiply(prev_el, el):
    return prev_el * el

print(reduce(multiply, [n for n in range(100, 1000, 2)]))


#вариант решения:

print(reduce(lambda prev_el, el: prev_el * el, [n for n in range(100, 1000, 2)]))
