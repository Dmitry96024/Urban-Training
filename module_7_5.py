import tkinter, os ,time
from tkinter import *

def poisk_file(*args):
    for root, dirs, files in os.walk(vvod1.get()):
        for file in files:
            if file.endswith(vvod.get()):
                filepath = os.path.abspath(file)
                filetime = os.path.getatime(file)
                formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
                filesize = os.path.getsize(file)
                parent_dir = os.path.dirname(filepath)
                window2 = tkinter.Tk()
                window2.title('Файл найден:')
                window2.geometry('500x250')
                window2.resizable(True, True)
                vyvod = tkinter.Label(window2, text=f'Обнаружен файл: {file}', height=2, width=50)
                vyvod.grid(row=1)
                vyvod1 = tkinter.Label(window2, text=f'Путь: {filepath}',height=2, width=50)
                vyvod1.grid(row=2)
                vyvod2 = tkinter.Label(window2, text=f'Размер: {filesize} байт', height=2, width=50)
                vyvod2.grid(row=3)
                vyvod3 = tkinter.Label(window2, text=f'Время изменения: {formatted_time}', height=2, width=50)
                vyvod3.grid(row=4)
                vyvod4 = tkinter.Label(window2, text=f'Родительская директория: {parent_dir}', height=2, width=70)
                vyvod4.grid(row=5)
                window2.mainloop()


window = tkinter.Tk()
window.title('Поиск файлов')
window.geometry('300x270')
window.resizable(False, False)
text1 = tkinter.Label(window, text='Введи имя файла с расширением для поиска ', height=5, width=40)
text1.grid(column = 1, row = 1 )
text1 = tkinter.Label(window, text='Введи директорию для поиска (например D:) ', height=5, width=40)
text1.grid(column = 1, row = 3 )
vvod = Entry(window, width = 30)
vvod.grid(column = 1, row = 2)
vvod1 = Entry(window, width = 30)
vvod1.grid(column = 1, row = 4)
text0 = tkinter.Label(window, text='', height=1, width=40)
text0.grid(column = 1, row = 5 )
btn = tkinter.Button(window, width= 10, text = 'Найти фаил', command = poisk_file)
btn.grid(column = 1, row = 6)

window.mainloop()


