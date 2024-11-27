'''
Цель: понять как работают потоки на практике, решив задачу

Задача "Потоковая запись в файлы":
Необходимо создать функцию write_words(word_count, file_name), где word_count - количество записываемых слов, file_name - название файла, куда будут записываться слова.
Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.
Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
В конце работы функции вывести строку "Завершилась запись в файл <название файла>".

После создания файла вызовите 4 раза функцию write_words, передав в неё следующие значения:
10, example1.txt
30, example2.txt
200, example3.txt
100, example4.txt
После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
10, example5.txt
30, example6.txt
200, example7.txt
100, example8.txt
Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
Также измерьте время затраченное на выполнение функций и потоков. Как это сделать рассказано в лекции к домашнему заданию.

'''

from time import sleep
from threading import Thread
from datetime import datetime


def wite_words(word_count, file_name):
    for i in range(1, word_count + 1):
        with open(file_name, 'a', encoding="utf-8") as file:
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')


time_start1 = datetime.now()
wite_words(10, '../example1.txt')
wite_words(30, '../example2.txt')
wite_words(200, '../example3.txt')
wite_words(100, '../example4.txt')
time_end1 = datetime.now()
time_res1 = time_end1 - time_start1

print(time_res1)

time_start2 = datetime.now()
the_f1 = Thread(target=wite_words, args=(10, "example5.txt"))
the_f2 = Thread(target=wite_words, args=(30, "example6.txt"))
the_f3 = Thread(target=wite_words, args=(200, "example7.txt"))
the_f4 = Thread(target=wite_words, args=(100, "example8.txt"))

the_f1.start()
the_f2.start()
the_f3.start()
the_f4.start()

the_f1.join()
the_f2.join()
the_f3.join()
the_f4.join()
time_end2 = datetime.now()
time_res2 = time_end2 - time_start2

print(time_res2)
