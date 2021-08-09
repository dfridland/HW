# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
#
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

# first solution:
with open("third.txt", "r", encoding="utf-8") as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Average salary is {sum(employees_dict.values()) / len(employees_dict)}\n'
          f'Employees with a salary less than 20k {[r[0] for r in employees_dict.items() if r[1] < 20000]}')

# 2nd solution:
def task():
    salary = {}
    with open('third.txt', 'r', encoding="utf-8") as f:
        for line in f:
            salary[line.split()[0]] = float(line.split()[1])
    print(f'Average salary is {sum(salary.values()) / len(salary)}\n'
          f'Salaries less than 20k: ')
    for name, salary in salary.items():
        if salary < 20000:
            print(name, salary)


task()
