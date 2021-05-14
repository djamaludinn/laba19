#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *


# Создаем функцию выбора радиокнопки
def change():
    if var.get() == 0:
        label['text'] = 'Aboba'
    elif var.get() == 1:
        label['text'] = 'Amogus'
    elif var.get() == 2:
        label['text'] = 'Brawl Stars'


if __name__ == '__main__':

    # Создаем графический интерфейс
    root = Tk()
    root.title('Радиокнопки')
    root.geometry('400x250')

    # Создаем радиокнопки
    var = IntVar()
    var.set(0)

    First = Radiobutton(text="First", variable=var, value=0, indicatoron=0, height=4, width=18, command=change)
    Second = Radiobutton(text="Second", variable=var, value=1, indicatoron=0, height=4, width=18, command=change)
    Third = Radiobutton(text="Third", variable=var, value=2, indicatoron=0, height=4, width=18, command=change)

    # Создаем метку
    label = Label(width=20, height=4)

    # Выводим радиокнопки
    First.grid(row=1, column=1, ipady=6)
    Second.grid(row=2, column=1, ipady=6)
    Third.grid(row=3, column=1, ipady=6)

    # Выводим метку
    label.grid(row=2, column=2, padx=60)

    # Запуск программы
    root.mainloop()
