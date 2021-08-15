#1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('first_1.txt', 'w', encoding="ascii") as f:
    while (line := input('Enter a new string or press enter to complete: ')) != "":
        print(line, file=f)
