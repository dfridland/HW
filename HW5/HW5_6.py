my_schedule = {}
with open('text6.txt', 'r', encoding='ascii') as f:
    for line in f:
        subject, hours = line.split(":")
        hour_per_subject = sum(map(int, "".join(i for i in hours if i == " " or "9" >= i >="0").split()))
        my_schedule[subject] = hour_per_subject
print(f' Total hours by subject: {my_schedule}')



