# 3 - one more solution:
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
