# Создать (программно) текстовый файл, записать в него программно
# набор чисел, разделенных пробелами. Программа должна подсчитывать
# сумму чисел в файле и выводить ее на экран.

from random import randint

with open('text5.txt', 'w+', encoding='ascii') as f:

    f.write(' '.join(str(randint(1, 100)) for el in range(100)))
    f.seek(0)
    print(f'Sum of randomly selected numbers is: {sum(map(int, f.readline().split() ))}')