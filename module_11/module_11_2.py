'''
Выберите одну или несколько сторонних библиотек Python, например, requests, pandas, numpy, matplotlib, pillow.
После выбора библиотек(-и) изучите документацию к ней(ним), ознакомьтесь с их основными возможностями и функциями.
К каждой библиотеке дана ссылка на документацию ниже.
Если вы выбрали:
requests - запросить данные с сайта и вывести их в консоль.
pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль.
numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.
matplotlib - визуализировать данные с помощью библиотеки любым удобным для вас инструментом из библиотеки.
pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.
'''
from sympy import Matrix, pprint
import numpy
import matplotlib.pyplot as plt

def print_row_reduced_matrix(matrix):
    print("Ступенчатая матрица метод Гауса:")
    pprint(matrix)

# выполняем сложение двух матриц

matrix1 = numpy.array([
    [1, 2, 3, 4],
    [4, 5, 6, 5],
    [7, 8, 9, 5],
    [5, 6, 7, 3]
])

matrix2 = numpy.array([
    [4, 5, 6, 5],
    [8, 1, 8, 8],
    [9, 2, 8, 7],
    [4, 5, 6, 5]
])

result = matrix1 + matrix2

# Определение расширенной матрицы [A|B]
augmented_matrix = Matrix(result)
print(augmented_matrix)

# Выполнение приведения матрицы к ступенчатому виду
row_reduced_matrix, _ = augmented_matrix.rref()

# Вызов функции для вывода ступенчатой матрицы
print_row_reduced_matrix(row_reduced_matrix)
otvet =  (row_reduced_matrix)[:,3]
print("Ответ: ", otvet)

#рисуем график

list_ = otvet
y = list_
x = range(len(y))
plt.plot(x, y)
plt.show()
