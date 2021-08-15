

rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open('text4_1.txt', 'w', encoding='utf-8') as new_f:
    with open('text4.txt', 'r', encoding="utf-8") as f:
        new_f.writelines([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in f])



