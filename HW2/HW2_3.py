#Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

#Dictionary solutiom:

month = int(input(" Enter a month in number format (from 1 to 12):  "))

my_dict = {1: 'January', 2: 'February', 3: 'March',  4: 'April',  5: 'May', 6: 'June', 7: 'July',
           8: 'August', 9: 'September', 10: 'October',  11: 'November', 12: 'December'}

if month in my_dict:
    print(f"{'you entered month'} {month}{'. It is'} {my_dict[month]}.")

my_dict_1 = {1: 'Winter', 2: 'Winter', 12: 'Winter', 3: "Spring",  4: "Spring",  5: "Spring", 6: "Summer",
             7: "Summer", 8: "Summer", 9: "Fall", 10: "Fall", 11: "Fall"}
if month in my_dict_1:
    print(f'{my_dict[month]}{" is in"} {my_dict_1[month]}.')
else:
    print("wrong number")

# решение без списка и без словаря
month = int(input(" Enter a month in number format (from 1 to 12):  "))

if 1 <= month <= 2  or month == 12:
       print("winter")
elif 3 <= month <= 5:
        print("spring")
elif 6 <= month <= 8:
        print("summer")
elif 9 <= month <= 11:
        print("Fall")

#List рещение, но можно сделать так и для словаря
while True:
    month = input(" Enter a month in number format (from 1 to 12):  ")
    if month.isdigit() and 0 < int(month) <= 12:
        season_list = ['winter', 'spring', 'summer', 'fall', "winter"]
        print(f'{season_list[int(month) // 3]}')
        break