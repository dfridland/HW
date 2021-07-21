#4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
#Hello my presious friends

my_str = input("Enter any sentence:  ").split()

for i, el in enumerate(my_str, 1):
    print(f'{i} {el[:10]}')

#другое рещение -
my_str = input("Enter any sentence:  ").split()

for i, el in enumerate(my_str, 1):
    print(i, el) if len(el) <= 10 else print(i, el[:10])