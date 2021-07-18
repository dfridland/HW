#HW lesson 15.07.2021
#1Работа с переменными

#name = input('What is your name?')
#print('Hello', name)
#age = int(input("how old are you?"))
#number = int(input("enter number from 0 to 10"))
#print(number, 'times 2 is', number*2)
#is_like = input('Do you like to study Python?')
#print('in 8 lessons you will know Python better')

#2 hh:mm:ss

#time = float(input("enter time in seconds"))
#day = time // (24 * 3600)
#time = time % (24 * 3600)
#hour = time // 3600
#time %= 3600

#min = time // 60
#time %= 60
#seconds = time
#print("d:h:m:s-> %d:%d:%d:%d" %(day, hour, min, seconds))

#3

#number = int(input('Enter a number: '))
#n1 = int('%s' % number)
#n2 = int("%s%s" % (number, number))
#n3 = int("%s%s%s" % (number, number, number))
#print(n1 + n2 + n3)

#4 biggest digit in a number

#number = int(input('Enter a number:  '))
#big = 0
#while number > 0:
  # q = number % 10
  # if q > big:
     #  big = q
  # number = number // 10
#print("big digit is", big)

#5
#revenue = int(input("Выручка в этом мес:  "))
#expenses = int(input('Издержки фирмы:  '))
#profit = revenue - expenses
#if revenue > expenses:
 #   print("profit =", profit)
  #  print('Фирма работает с прибылью')
   # profit_margit = profit / revenue
    #print('Рентабильность выручки', profit_margit)
    #number_employees =int(input('Число сотрудников в фирме?  '))
    #nipe = profit / number_employees
    #print("Прибыль фирмы в расчете на одного сотрудника", nipe)
#else:
 #   print("profit =", revenue - expenses)
  #  print('Фирма работает с убытками')

  #6


#a = int(input('Сколько километров пробежал спортсмен в первый день?  '))
#b = int(input('Сколько километров пробежал спортсмен в последний день?  '))
#c = 1
#while a < b:
 #   a*= 1.1
  #  c+= 1
#print("Спортсмен достиг результата в", b, "км на", c, "день")