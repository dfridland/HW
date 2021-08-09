#4 Программа принимает действительное
# положительное число
# x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без
# встроенной функции возведения числа в степень.

#Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **. В
# торой — более сложная реализация без оператора **,
# предусматривающая использование цикла.

def my_func(x, y):

     if y < 0:
        result = x**y
        print(result)
     else:

        print("Exponent has to be negative")

(my_func(x = int(input("Enter a number:  ")),
         y = int(input("Enter a negative exponent:  "))))



#другое решение:

def my_f(a, n):
    res = 1

    for i in range(abs(n)):
        res *= a
    if n < 0:
        return 1 / res
    else:
        return "Exponent has to be negative"

print(my_f(int(input("Enter:  ")), int(input("Enter:  "))))




