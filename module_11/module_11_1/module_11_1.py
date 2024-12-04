import matplotlib.pyplot as plt
import csv


x_axis= float(input(f'enter the x-axis offset: '))
y_axis= float(input(f'enter the y-axis offset: '))


X = []
Y = []
X1 = []
Y1 = []
X2 = []
Y2 = []


with open("test2.csv", 'r') as datafile:

    plotting = csv.reader(datafile, delimiter=';') # или , если в ячейке
    next(plotting)
    for row in plotting:
        #X.append(float(row[0].replace(',', '.'))) # необходимо для 2 столбцов
        Y.append(float(row[0].replace(',', '.')))


    for i in range(len(Y)):
           X1.append(i + x_axis)
           X2.append(i - x_axis)
    for j in Y:
            Y1.append(j * y_axis)
            Y2.append(j / y_axis)

    X = range(len(Y))

# Здесь отображается график по тем осям которые необходимы
#    plt.subplot(2, 2, 1) это построение нескольких графиков в 1 окне
    plt.plot(X, Y)
#plt.subplot(2, 2, 2) #это построение нескольких графиков в 1 окне

    plt.plot(X1, Y)
    plt.plot(X2, Y)
    plt.plot(X, Y1)
    plt.plot(X, Y2)
    plt.title('offset')
    plt.show()
