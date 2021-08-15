class MyOwnErr(Exception):
    def __init__(self, txt):  #why i need it here?
        self.txt = txt

one = int(input("Enter number:  "))
two = int(input("Enter number:  "))
try:
    if two == 0:
        raise MyOwnErr("There is no division by zero")
except (ValueError, MyOwnErr) as err:
    print(err)
else:
    print(one / two)
