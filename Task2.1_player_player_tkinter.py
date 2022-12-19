# Игра: человек против человека
#
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, # чтобы забрать все конфеты у своего конкурента?
#
from tkinter import *
from tkinter import messagebox as mb
from tkinter import font, ttk
from random import randint
root = Tk()
root.title("Игра с конфетами")
root.geometry("370x250+700+500")
root.resizable(width=False, height=False)

l5 = Label(text='А', font=("Arial Black", 10), bg="lightgreen", fg="blue")
l5.grid(row=1, column=1)
l6 = Label(text='Б', font=("Arial Black", 10), bg="lightgreen", fg="blue")
l6.grid(row=1, column=5)
l7 = Label(text='2021', font=("Arial Black", 10))
l7.grid(row=6, column=4)
l8 = Label(text='число оставшихся конфет', font=("Arial", 10))
l8.grid(row=5, column=4)

rand = randint(0, 1)
if rand == 0:
    l = Label(text='Игру начинает игрок А', font=(
        "Arial Black", 10), bg="lightgreen", fg="blue")
    l1 = Label(text='Введите кол-во конфет\n(максимум 28)\nв поле А и нажмите кнопку 1', font=(
        "Arial", 11))
elif rand == 1:
    l = Label(text='Игру начинает игрок Б', font=(
        "Arial Black", 10), bg="lightgreen", fg="blue")
    l1 = Label(text='Введите кол-во конфет\n(максимум 28)\nв поле Б и нажмите кнопку 2', font=(
        "Arial", 11))
l.grid(row=1, column=4)
l1.grid(row=2, column=4)

get1, get2 = 0, 0
v1 = IntVar()
v2 = IntVar()
x = 2021
t = 0

e1 = Entry(textvariable=v1, width=8, justify=CENTER,
           font=font.Font(family="Arial Black", size=10))
e2 = Entry(textvariable=v2, width=8, justify=CENTER,
           font=font.Font(family="Arial Black", size=10))

b1 = Button(text="1", width=7, height=1)
b2 = Button(text="2", width=7, height=1)


def check_mistake(_get, _e):
    global rand
    if _get <= 28 and _get > 0:
        if rand == 0:
            l2 = Label(text='Ход игрока Б',
                       font=("Arial Black", 11), bg="lightblue", fg="blue")
            rand = 1
            l2.grid(row=3, column=4)
        elif rand == 1:
            l2 = Label(text='Ход игрока А',
                       font=("Arial Black", 11), bg="lightblue", fg="blue")
            rand = 0
            l2.grid(row=3, column=4)
    else:
        mb.showerror("Ошибка", "Можно брать от 1 до 28 конфет")
        _e.delete(0, END)
    return rand


def winner():
    if t == 1 and x <= 0:
        l3 = Label(text='Победитель - игрок А',
                   font=("Arial Black", 12), bg="red", fg="lightblue")
        l3.grid(row=8, column=4)
    elif t == 2 and x <= 0:
        l3 = Label(text='Победитель - игрок Б',
                   font=("Arial Black", 12), bg="red", fg="lightblue")
        l3.grid(row=8, column=4)


def enter1(event):
    global get1, t, x
    get1 = v1.get()
    check_mistake(get1, e1)
    x = x - get1
    if x < 0:
        l7["text"] = 0
    else:
        l7["text"] = x
    t = 1
    e1.delete(0, END)
    winner()


def enter2(event):
    global get2, t, x
    get2 = v2.get()
    check_mistake(get2, e2)
    x = x - get2
    if x < 0:
        l7["text"] = 0
    else:
        l7["text"] = x
    t = 2
    e1.delete(0, END)
    winner()


b1.bind('<Button-1>', enter1)
b2.bind('<Button-1>', enter2)

e1.grid(row=2, column=1)
e2.grid(row=2, column=5)
b1.grid(row=3, column=1)
b2.grid(row=3, column=5)

root.mainloop()
