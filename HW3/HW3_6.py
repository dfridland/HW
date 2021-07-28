# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских
# букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.


# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def my_func():

    word = input("Enter a word in lowercase letters:  ")
    print(word.title())
    words = input("Enter a sentence with words only in lowercase letters:  ")
    print(words.title())


my_func()


# еще вариант:


def my_f(word):

    return word.title()


print(my_f(input("enter word: ")))
print(my_f(input("enter sent: ")))
