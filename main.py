year = int(input("Введите год: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} год является високосным годом.")
else:
    print(f"{year} год является невисокосным годом.")
