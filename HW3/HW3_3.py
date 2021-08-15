# 3 Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


my_f = lambda a, b, c: (a + b + c) - min(a, b, c)

print(my_f(5, 2, 6))


# еше вариант:


def my_fun(n, m, k):

    return sum(sorted([n, m, k])[1:])


print(my_fun(int(input("Enter 1st number:  ")), int(input("Enter 2nd number:  ")),
             int(input("Enter 3rd number: "))))
