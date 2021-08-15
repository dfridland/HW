#3

number = int(input('Enter a single digit number: '))
n1 = int('%s' % number)
n2 = int("%s%s" % (number, number))
n3 = int("%s%s%s" % (number, number, number))
print(number, " + ", number,number," + ",number,number,number," = ",n1 + n2 + n3)
