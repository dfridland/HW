#5
revenue = int(input("Выручка в этом мес:  "))
expenses = int(input('Издержки фирмы:  '))
profit = revenue - expenses
if revenue > expenses:
    print("profit =", profit)
    print('Фирма работает с прибылью')
    profit_margit = profit / revenue
    print('Рентабильность выручки', profit_margit)
    number_employees =int(input('Число сотрудников в фирме?  '))
    nipe = profit / number_employees
    print("Прибыль фирмы в расчете на одного сотрудника", nipe)
else:
    print("profit =", revenue - expenses)
    print('Фирма работает с убытками')