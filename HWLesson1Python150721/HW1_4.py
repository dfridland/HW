#4 biggest digit in a number

number = int(input('Enter a Multi-Digit number:  '))
big = 0
while number > 0:
   q = number % 10
   if q > big:
       big = q
   number = number // 10
print("big digit is", big)
