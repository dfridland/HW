#1

def my_f():

    try:
        n_1 = int(input("Enter 1st number: "))
        n_2 = int(input("Enter 2nd number: "))
        div = n_1 / n_2
        print(div)
    except ZeroDivisionError as err:
       print(f"{'Error!'} {err}")

my_f()
