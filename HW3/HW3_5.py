# 5. Программа запрашивает у пользователя строку чисел,
# разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def my_f():

    s = 0
    while True:
        a = (input("enter a few numbers separated by backspace, input Q to exit: ")).split()
        for num in a:
            if num == "Q":

                return s
            else:
                s += int(num)
        print(s)


print(my_f())
