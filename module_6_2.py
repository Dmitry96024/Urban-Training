"""
Задача "Изменять нельзя получать":
В этой задаче мы реализуем классы транспорта, в которых нельзя будет просто так поменять цвет, мощность двигателя и прочие свойства, т.к. в реальной жизни это чаще всего делается не владельцем, а в специальных сервисах. Да, узнать значения этих свойств мы сможем, но вот изменить - нет.

Вам необходимо создать 2 класса: Vehicle и Sedan, где Vehicle - это любой транспорт, а Sedan(седан) - наследник класса Vehicle.

I. Каждый объект Vehicle должен содержать следующие атрибуты объекта:
Атрибут owner(str) - владелец транспорта. (владелец может меняться)
Атрибут __model(str) - модель (марка) транспорта. (мы не можем менять название модели)
Атрибут __engine_power(int) - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
Атрибут __color(str) - название цвета. (мы не можем менять цвет автомобиля своими руками)
А так же атрибут класса:
Атрибут класса __COLOR_VARIANTS, в который записан список допустимых цветов для окрашивания. (Цвета написать свои)
Каждый объект Vehicle должен содержать следующий методы:
Метод get_model - возвращает строку: "Модель: <название модели транспорта>"
Метод get_horsepower - возвращает строку: "Мощность двигателя: <мощность>"
Метод get_color - возвращает строку: "Цвет: <цвет транспорта>"
Метод print_info - распечатывает результаты методов (в том же порядке): get_model, get_horsepower, get_color; а так же владельца в конце в формате "Владелец: <имя>"
Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color, если он есть в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".
Взаимосвязь методов и скрытых атрибутов:
Методы get_model, get_horsepower, get_color находятся в одном классе с соответствующими им атрибутами: __model, __engine_power, __color. Поэтому атрибуты будут доступны для методов.
Атрибут класса __COLOR_VARIANTS можно получить обращаясь к нему через объект(self).
Проверка в __COLOR_VARIANTS происходит не учитывая регистр ('BLACK' ~ 'black').
II. Класс Sedan наследуется от класса Vehicle, а так же содержит следующие атрибуты:
Атрибут __PASSENGERS_LIMIT = 5 (в седан может поместиться только 5 пассажиров)

Пункты задачи:
Создайте классы Vehicle и Sedan.
Напишите соответствующие свойства в обоих классах.
Не забудьте сделать Sedan наследником класса Vehicle.
Создайте объект класса Sedan и проверьте, как работают все его методы, взяты из класса Vehicle.

Пример результата выполнения программы:
Исходный код:
# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
"""

class Vehicle:
    __COLOR_VARIANTS = ['Black', 'Yellow', 'White', 'Grin', 'Red', 'Blue']
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)
        self.__model = str (__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color.upper()}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}\n')

    def set_color(self, new_color):
        # new_color = input('Новый цвет: ')
        reg_colours = [colour.lower() for colour in self.__COLOR_VARIANTS] # для проверки без учета регистра
        if new_color.lower() in reg_colours:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}\n')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 4

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan ('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
