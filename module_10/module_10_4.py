'''
Задача "Потоки гостей в кафе":
Необходимо имитировать ситуацию с посещением гостями кафе.
Создайте 3 класса: Table, Guest и Cafe.
Класс Table:
Объекты этого класса должны создаваться следующим способом - Table(1)
Обладать атрибутами number - номер стола и guest - гость, который сидит за этим столом (по умолчанию None)
Класс Guest:
Должен наследоваться от класса Thread (быть потоком).
Объекты этого класса должны создаваться следующим способом - Guest('Vasya').
Обладать атрибутом name - имя гостя.
Обладать методом run, где происходит ожидание случайным образом от 3 до 10 секунд.
Класс Cafe:
Объекты этого класса должны создаваться следующим способом - Cafe(Table(1), Table(2),....)
Обладать атрибутами queue - очередь (объект класса Queue) и tables - столы в этом кафе (любая коллекция).
Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей).
Метод guest_arrival(self, *guests):
Должен принимать неограниченное кол-во гостей (объектов класса Guest).
Далее, если есть свободный стол, то садить гостя за стол (назначать столу guest), запускать поток гостя и выводить на экран строку
"<имя гостя> сел(-а) за стол номер <номер стола>".
Если же свободных столов для посадки не осталось, то помещать гостя в очередь queue и выводить сообщение "<имя гостя> в очереди".
Метод discuss_guests(self):
Этот метод имитирует процесс обслуживания гостей.
Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят.
Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive), то вывести строки
"<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и "Стол номер <номер стола> свободен". Так же текущий стол освобождается (table.guest = None).
Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None), то текущему столу присваивается гость взятый из очереди (queue.get()).
 Далее выводится строка "<имя гостя из очереди> вышел(-ла) из очереди и сел(-а) за стол номер <номер стола>"
Далее запустить поток этого гостя (start)
Таким образом мы получаем 3 класса на основе которых имитируется работа кафе:
Table - стол, хранит информацию о находящемся за ним гостем (Guest).
Guest - гость, поток, при запуске которого происходит задержка от 3 до 10 секунд.
Cafe - кафе, в котором есть определённое кол-во столов и происходит имитация прибытия гостей (guest_arrival) и их обслуживания (discuss_guests).
'''
import random, queue
from threading import Thread
from time import sleep

class Table():
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        pause =  random.randint(3, 10)
        sleep(pause)

class Cafe:
    list_thr = []

    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        list_guests = list(guests)
        list_tables = self.tables
        len_list_guests = len(list_guests)
        min_guests_tables = min(len_list_guests, len(self.tables))
        for i in range(min_guests_tables):
            list_tables[i].guest = guests[i]
            thr1 = guests[i]
            thr1.start()
            Cafe.list_thr.append(thr1)
            if list_guests[i].name == 'Nikita':
                print(f'{list_guests[i].name} сел за стол номер {list_tables[i].number}')
            elif list_guests[i].name[-1] == 'a':
                print(f'{list_guests[i].name} села за стол номер {list_tables[i].number}')
            else:
                print(f'{list_guests[i].name} сел за стол номер {list_tables[i].number}')
        if len_list_guests > min_guests_tables:
            for i in range(min_guests_tables, len_list_guests):
                self.queue.put(guests[i])
                print(f'{list_guests[i].name} в очереди')

    def discuss_guests(self):
        while not (self.queue.empty()) or Cafe.check_table(self):
            for table in self.tables:
                if not (table.guest is None) and not (table.guest.is_alive()):
                    if table.guest.name == 'Nikita':
                        print(f'{table.guest.name} покушал и ушёл')
                    elif table.guest.name[-1] =='a':
                        print(f'{table.guest.name} покушала и ушла')
                    else:
                        print(f'{table.guest.name} покушал и ушёл')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if (not (self.queue.empty())) and table.guest is None:
                    table.guest = self.queue.get()
                    if table.guest.name == 'Nikita':
                        print(f'{table.guest.name} вышел из очереди и сел за стол номер {table.number}')
                    elif table.guest.name[-1]== 'a':
                        print(f'{table.guest.name} вышла из очереди и села за стол номер {table.number}')
                    else:
                        print(f'{table.guest.name} вышел из очереди и сел за стол номер {table.number}')
                    thr1 = table.guest
                    thr1.start()
                    Cafe.list_thr.append(thr1)

    def check_table(self):
        for table in self.tables:
            if table.guest is not None:
                return True
        return False


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
# cafe.guest_arrival(*guests)
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
for thr in Cafe.list_thr:
    thr.join()

