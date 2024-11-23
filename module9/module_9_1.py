'''
Задача "Вызов разом":
Напишите функцию apply_all_func(int_list, *functions), которая принимает параметры:
int_list - список из чисел (int, float)
*functions - неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел)
Эта функция должна:
Вызвать каждую функцию к переданному списку int_list
Возвращать словарь, где ключом будет название вызванной функции, а значением - её результат работы со списком int_list.
Пункты задачи:
В функции apply_all_func создайте пустой словарь results.
Переберите все функции из *functions.
При переборе функций записывайте в словарь results результат работы этой функции под ключом её названия.
Верните словарь results.
Запустите функцию apply_all_func, передав в неё список из чисел и набор других функций.
Пример результата выполнения программы:
В примере используются следующие функции:
min - принимает список, возвращает минимальное значение из него.
max - принимает список, возвращает максимальное значение из него.
len - принимает список, возвращает кол-во элементов в нём.
sum - принимает список, возвращает сумму его элементов.
sorted - принимает список, возвращает новый отсортированный список на основе переданного.

'''
def apply_all_func(int_list, *functions):
    results = {}

    for i in functions:
        results[i.__name__] = i(int_list)

    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
