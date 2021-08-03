# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open("second.txt", "r", encoding="ascii") as f:
    number_of_lines = 0
    number_of_words = 0
    number_of_characters = 0
    for line in f:
        line = line.strip('\n')
        words = line.split()
        number_of_lines += 1
        number_of_words += len(words)
        number_of_characters += len(line)
print(f'{"lines:", number_of_lines, "words:", number_of_words, "characters:", number_of_characters}')


# решение

print("Solution 1")

with open("second.txt", "r", encoding="ascii") as f:
    result = [f'{line}.{" ".join(count.split())} - {len(count.split())} words' for line, count in
              enumerate(f, 1)]
    print(*result, f'There are {len(result)} lines in the text.', sep='\n')

#
print("Solution 2")

with open("second.txt", "r", encoding="ascii") as f:
    text = f.readlines()
    for i, value in enumerate(text, 1):
        number_of_words = len(value.split())
        print(f'Line {i} has {number_of_words} words.')



