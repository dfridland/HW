#2
def my_f():
    s_1 = input("Enter your name: ")
    s_2 = input("What year were you born: ")
    s_3 = input("Where do you live: ")
    s_4 = input("What is your email ")
    s_5 = input("What is your cell phone number: ")

    return (f"{'My name is'} {s_1}, {'I was born in'} {s_2}"
            f"{'.  I live in'} {s_3}{'.  My email is  '} {s_4}"
            f"{'.  My cell phone is  '}{s_5}")

print(my_f())


