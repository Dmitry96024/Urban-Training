print("Необходимо ввести три целых числа")
first = int(input("Введи первое целое число:",))
second = int(input("Введи второе целое число:",))
third = int(input("Введи третье целое число:",))
if first==second==third:
    print(3, " (Все числа равны)")
elif first==third:
    print(2, " (Два числа равны)")
elif second==third:
    print(2, " (Два числа равны)")
else: print(0, " (Нет равных чисел)")