import random

trials = 10000
same_birthdays=0

for _ in range(trials):
    birthdays = []
    for i in range(70):
        birthday = random.randint(1,365)
        if birthday in birthdays:
            same_birthdays += 1
            break
        birthdays.append(birthday)

print(f'{same_birthdays/ trials * 100}%')
