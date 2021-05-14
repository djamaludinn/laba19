#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *


# Создаем функцию для загрузки файла
def load():
    text = entry.get()
    with open(f'{text}', 'r') as f:
        result = soul.insert(0.1, f.read())
        return result


# Создаем функцию для сохранения файла
def save():
    form = soul.get(0.1, 'end')
    text = entry.get()
    with open(f'{text}', 'r+') as f:
        f.write(form)


if __name__ == '__main__':

    # Создаем графический интерфейс
    root = Tk()
    root.title('Открытие и сохранение файла')
    root.geometry('1000x500')

    # Создаем формы для ввода значений
    entry = Entry(root, width=20, font=36)

    # Создаем кнопки для выполнений определенных команд
    button_red = Button(height=1, width=20, text='Открыть', command=load)
    button_orange = Button(height=1, width=20, text='Сохранить', command=save)

    # Создаем поле для ввода большого текста
    soul = Text(root, width=200, height=50, bg="#8DE1DD", fg='white', wrap=WORD, font=12)

    # Делаем вывод наших полей
    entry.place(x=1, y=10)
    button_red.place(x=186, y=8)
    button_orange.place(x=335, y=8)
    soul.place(x=1, y=35)


    # Запуск программы
    root.mainloop()
