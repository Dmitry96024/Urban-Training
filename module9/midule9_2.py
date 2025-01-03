'''

Задача:
Даны несколько списков, состоящих из строк
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
В переменную first_result запишите список созданный при помощи сборки состоящий из длин строк списка first_strings, при условии, что длина строк не менее 5 символов.
В переменную second_result запишите список созданный при помощи сборки состоящий из пар слов(кортежей) одинаковой длины. Каждое слово из списка
first_strings должно сравниваться с каждым из second_strings. (два цикла)
В переменную third_result запишите словарь созданный при помощи сборки, где парой ключ-значение будет строка-длина строки. Значения строк
будут перебираться из объединённых вместе списков first_strings и second_strings. Условие записи пары в словарь - чётная длина строки.

Пример результата выполнения программы:
Пример выполнения кода:
print(first_result)
print(second_result)
print(third_result)
Вывод на консоль:

Примечания:
Помните, когда вы используете 2 цикла for внутри сборки, первый цикл - внешний, второй - внутренний.
'''

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
first_result = [len(i) for i in first_strings if len(i) >= 5 ]
second_result = {(i,j) for i in first_strings for j in second_strings if len(i) == len(j) }
third_result = {i:len(i) for i in (first_strings + second_strings) if len(i) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)