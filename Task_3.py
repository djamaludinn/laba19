#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *


# Создаем функции для выбора цветов
def color_red():
    label['text'] = 'Красный'
    text.delete(0, "end")
    text.insert(0, '#ff0000')


def color_orange():
    label['text'] = 'Оранжевый'
    text.delete(0, "end")
    text.insert(0, '#ff7d00')


def color_yellow():
    label['text'] = 'Желтый'
    text.delete(0, "end")
    text.insert(0, '#ffff00')


def color_green():
    label['text'] = 'Зеленый'
    text.delete(0, "end")
    text.insert(0, '#00ff00')


def color_blue():
    label['text'] = 'Голубой'
    text.delete(0, "end")
    text.insert(0, '#007dff')


def color_drblue():
    label['text'] = 'Синий'
    text.delete(0, "end")
    text.insert(0, '#0000ff')


def color_purple():
    label['text'] = 'Фиолетовый'
    text.delete(0, "end")
    text.insert(0, '#7d00ff')


if __name__ == '__main__':

    # Создаем графический интерфейс
    root = Tk()
    root.title('Цвета радуги')
    root.geometry('217x100')

    # Вывод значений.
    label = Label(root, text='', font=32)
    label.pack()

    # Создаем формы для ввода значений
    text = Entry(root, width=55, font=36, justify=CENTER)

    # Выводим формы друг под другом
    text.pack(ipady=10, pady=2)

    # Создаем кнопки для выполнений определенных команд
    button_red = Button(root, width=3, height=20, bg='#ff0000', command=color_red)
    button_orange = Button(root, width=3, height=20, bg='#ff7d00', command=color_orange)
    button_yellow = Button(root, width=3, height=20, bg='#ffff00', command=color_yellow)
    button_green = Button(root, width=3, height=20, bg='#00ff00', command=color_green)
    button_blue = Button(root, width=3, height=20, bg='#007dff', command=color_blue)
    button_drblue = Button(root, width=3, height=20, bg='#0000ff', command=color_drblue)
    button_purple = Button(root, width=3, height=20, bg='#7d00ff', command=color_purple)

    # Выводим кнопки друго под другом
    button_red.pack(side=LEFT)
    button_orange.pack(side=LEFT)
    button_yellow.pack(side=LEFT)
    button_green.pack(side=LEFT)
    button_blue.pack(side=LEFT)
    button_drblue.pack(side=LEFT)
    button_purple.pack(side=LEFT)

    # Запуск программы
    root.mainloop()

