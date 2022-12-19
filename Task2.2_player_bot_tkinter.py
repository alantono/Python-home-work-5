# Игра: человек против бота
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, # чтобы забрать все конфеты у своего конкурента?
#
from tkinter import *
from tkinter import messagebox as mb
from tkinter import font, ttk
from random import randint
root = Tk()
root.title("Игра с конфетами. Человек против бота")
root.geometry("370x250+700+500")
root.resizable(width=False, height=False)

l5 = Label(text='Человек', font=("Arial Black", 10),
           bg="lightgreen", fg="blue")
l5.grid(row=1, column=1)
l6 = Label(text='Бот', font=("Arial Black", 10), bg="lightgreen", fg="blue")
l6.grid(row=1, column=5)
l7 = Label(text='2021', font=("Arial Black", 10))
l7.grid(row=6, column=4)
l8 = Label(text='число оставшихся конфет', font=("Arial", 10))
l8.grid(row=5, column=4)

rand = randint(0, 1)
if rand == 0:
    l = Label(text='Игру начинает Человек', font=(
        "Arial Black", 10), bg="lightgreen", fg="blue")
    l1 = Label(text='Введите кол-во конфет\n(максимум 28)\nв поле А и нажмите кнопку 1', font=(
        "Arial", 11))
elif rand == 1:
    l = Label(text='Игру начинает Бот', font=(
        "Arial Black", 10), bg="lightgreen", fg="blue")
    l1 = Label(text='Введите кол-во конфет\n(максимум 28)\nв поле А и нажмите кнопку 1', font=(
        "Arial", 11))
l.grid(row=1, column=4)
l1.grid(row=2, column=4)

get1 = 0
v1 = IntVar()
v2 = IntVar()
n = 2021

e1 = Entry(textvariable=v1, width=8, justify=CENTER,
           font=font.Font(family="Arial Black", size=10))
e2 = Entry(textvariable=v2, width=8, justify=CENTER,
           font=font.Font(family="Arial Black", size=10))
b1 = Button(text="1", width=7, height=1)


def check_mistake():
    global get1
    if int(get1) > 28:
        mb.showerror("Ошибка", "Можно брать от 1 до 28 конфет")
        e1.delete(0, END)


def bot_step():  # ходит бот
    global n, k
    if n <= 28 and n > 0:
        e2.insert(INSERT, n)
        l7["text"] = 0
        l3 = Label(text='Победитель - бот',
                   font=("Arial Black", 12), bg="red", fg="lightblue")
        l3.grid(row=8, column=4)
    else:
        k = 29 - int(get1)
        n = n - k
        l7["text"] = n
        e2.delete(0, END)
        e2.insert(INSERT, k)
        l2 = Label(text='Ваш ход',
                   font=("Arial Black", 11), bg="lightblue", fg="blue")
        l2.grid(row=3, column=4)
        e1.delete(0, END)


def enter1(event):
    global get1, n, e1
    get1 = v1.get()
    check_mistake()
    n = n - get1
    l7["text"] = n
    bot_step()
    if n == 0:
        l3 = Label(text='Вы победили', font=(
            "Arial Black", 12), bg="red", fg="lightblue")
        l3.grid(row=8, column=4)


if rand == 1:
    e2.delete(0, END)
    e2.insert(INSERT, "20")
    n = int(n) - 20
    l7["text"] = n
    l2 = Label(text='Ваш ход',
               font=("Arial Black", 11), bg="lightblue", fg="blue")
    l2.grid(row=3, column=4)

b1.bind('<Button-1>', enter1)

e1.grid(row=2, column=1)
e2.grid(row=2, column=5)
b1.grid(row=3, column=1)

root.mainloop()
