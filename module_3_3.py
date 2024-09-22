#1.Функция с параметрами по умолчанию:
#Создайте функцию print_params(a = 1, b = 'строка', c = True),
# которая принимает три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True).
def print_params(a = 1, b = 'Строка', c = True ):
#Функция должна выводить эти параметры.
#Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
    print (a, b, c)
#Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
#2.Распаковка параметров:
#Создайте список values_list с тремя элементами разных типов.
vallues_list = [1, 'Строка', True]
#Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
values_dict = {'a': 1, 'b': "строка", 'c': False}
#Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
print_params(*vallues_list)
print_params(**values_dict)
#3.Распаковка + отдельные параметры:
#Создайте список values_list_2 с двумя элементами разных типов
values_list_2 = [54.32, 'Строка' ]
#Проверьте, работает ли print_params(*values_list_2, 42)
print_params(*values_list_2, 42)
