class Data:

   def __init__(self, date):
       self.date = str(date)

   @classmethod
   def get_number(cls, date):
     my_date = []
     for i in date.split():
         if i != "-":
             my_date.append(i)
     return f'{int(my_date[0]), int(my_date[1]), int(my_date[2])}'

   @staticmethod
   def validation(day, month, year):
       if  1 <= day <=31:
           if 1 <= month <= 12:
               if year <= 2021:
                   return f'Date is correct'
               else:
                   return f' wrong year'
           else:
               return f' wrong month'
       else:
           return f' wrong day'

   def __str__(self):
       return f' today is {Data.get_number(self.date)}'

one = Data ('10 - 08 - 2021')
print(one)
print(Data.validation(11, 12, 2011))
print(Data.get_number("11 - 12 - 2011"))