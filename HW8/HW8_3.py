class MyOwnErr(Exception):
   pass
my_list = []
while True:
    try:
        value = input("Enter an element or Q to exit: ")
        if value == "Q":
            print(my_list)
            break
        if not value.isdigit():
            raise MyOwnErr("Not a Number")
    except (ValueError, MyOwnErr) as err:
         print(err)
    else:
        my_list.append(int(value))
        print(my_list)
