#Просим пользователя ввести год
year = int(input("Введите год: "))
#Проверяем, кратен ли год 4 и не кратен 100, или кратен 400.
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#Вывод значения в зависимости от года    
    print(f"{year} год является високосным годом.")
else:
    print(f"{year} год является невисокосным годом.")
