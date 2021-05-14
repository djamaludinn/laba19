#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *


# Создаем функцию сложения.
def sum():
    try:
        x = float(text1.get())
        y = float(text2.get())
        label.config(text="Вывод: {}".format(x + y))
    except ValueError:
        label.config(text="Ошибка. Введите числа!")


# Создаем функцию вычитания.
def sub():
    try:
        x = float(text1.get())
        y = float(text2.get())
        label.config(text="Вывод: {}".format(x - y))
    except ValueError:
        label.config(text="Ошибка. Введите числа!")


# Создаем функцию умножения.
def mul():
    try:
        x = float(text1.get())
        y = float(text2.get())
        label.config(text="Вывод: {}".format(x * y))
    except ValueError:
        label.config(text="Ошибка. Введите числа!")


# Создаем функцию деления.
def div():
    try:
        x = float(text1.get())
        y = float(text2.get())
        label.config(text="Вывод: {}".format(x / y))
    except ValueError:
        label.config(text="Ошибка. Введите числа!")


if __name__ == '__main__':

    # Создаем графический интерфейс
    root = Tk()
    root.title('Калькулятор')
    root.geometry('400x250')
    f_top = Frame(root)
    f_bot = Frame(root)

    # Создаем формы для ввода значений
    text1 = Entry(root, width=55, font=36, justify=CENTER)
    text2 = Entry(root, width=55, font=36, justify=CENTER)

    # Выводим формы друг под другом
    text1.pack(ipady=10, pady=2)
    text2.pack(ipady=10)

    # Создаем кнопки для выполнений определенных команд
    button_sum = Button(f_top, text='+', width=20, height=2, font=32, bg='#E10C04', fg='black', command=sum)
    button_sub = Button(f_top, text='-', width=20, height=2, font=32, bg='#0D1BE1', fg='black', command=sub)
    button_mul = Button(f_bot, text='*', width=20, height=2, font=32, bg='#0DE118', fg='black', command=mul)
    button_div = Button(f_bot, text='/', width=20, height=2, font=32, bg='#D60DE1', fg='black', command=div)

    # Выводим кнопки друго под другом
    f_top.pack()
    f_bot.pack()
    button_sum.pack(side=LEFT)
    button_sub.pack(side=LEFT)
    button_mul.pack(side=LEFT)
    button_div.pack(side=LEFT)

    # Вывод значений в метку
    label = Label(root, text="Вывод: ", font=32)
    label.pack()

    # Запуск программы
    root.mainloop()
