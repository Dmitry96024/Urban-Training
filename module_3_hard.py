# Создаём функцию
def calculate_structure_sum(data_structure):
    summ = 0
    # сумма key и value
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            summ += calculate_structure_sum(key)
            summ += calculate_structure_sum(value)
        # иначе сумма состоящаяя из списка,кортэжа,множества
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            summ += calculate_structure_sum(item)
        # иначе сумма - целого числа и числа с плавающей точкой
    elif isinstance(data_structure, (int, float)):
        summ += data_structure
        # summa - функции len
    elif isinstance(data_structure, str):
        summ += len(data_structure)
        # возврат из функции значения 'summ'
    return summ

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
# результат
result = calculate_structure_sum(data_structure)
print(result)
