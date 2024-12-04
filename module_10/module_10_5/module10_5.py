'''
Создайте функцию read_info(name), где name - название файла. Функция должна:
Создавать локальный список all_data.
Открывать файл name для чтения.
Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
Во время считывания добавлять каждую строку в список all_data.
Этих операций достаточно, чтобы рассмотреть преимущество многопроцессного выполнения программы над линейным.
Создайте список названий файлов в соответствии с названиями файлов архива.
Вызовите функцию read_info для каждого файла по очереди (линейно) и измерьте время выполнения и выведите его в консоль.
Вызовите функцию read_info для каждого файла, используя многопроцессный подход: контекстный менеджер with и объект Pool.
Для вызова функции используйте метод map, передав в него функцию read_info и список названий файлов. Измерьте время выполнения и выведите его в консоль.
Для избежания некорректного вывода запускайте линейный вызов и многопроцессный по отдельности, предварительно закомментировав другой.
'''

import multiprocessing, time
from os import cpu_count

def read_info(name):
    all_data = []

    '''
    # данный цикл чтения работает правильнее но дольше
    with open(name, 'r') as file:
        for line in file:
            all_data.append(line.strip())
    '''
    # а этот цикл по заданию
    with open(name, encoding="utf-8") as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break

filenames = [f'file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':

    a = time.time()
    for i in filenames:
        read_info(i)
    b = time.time()
    line = b - a
    print(f'Время работы линейного вызова : {line}')

    c =time.time()
    with multiprocessing.Pool(processes = cpu_count()) as pool:
        pool.map(read_info, filenames)

    d = time.time()
    mult = d - c
    print(f'Время работы мультипроцесса : {mult}')
