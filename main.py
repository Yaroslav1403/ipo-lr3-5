#Просим пользователя ввести год
year = int(input("Введите год: "))
#Проверяем, кратен ли год 4
if (year % 4 == 0):
#Вывод значения в зависимости от года    
    print(f"{year} год является високосным годом.")
else:
    print(f"{year} год является невисокосным годом.")
