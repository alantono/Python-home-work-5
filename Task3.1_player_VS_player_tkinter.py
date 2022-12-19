# Создайте программу для игры в ""Крестики-нолики"".
# игрок А против игрока Б
from tkinter import *
from tkinter import messagebox as mb
from tkinter import font, ttk
from random import randint
root = Tk()
root.title("Крестики Нолики")
root.geometry("450x450+700+500")
root.resizable(width=False, height=False)

rand = randint(0, 1)
if rand == 0:
    l = Label(text='Игру начинает игрок А', font=(
        "Arial Black", 10), bg="lightgreen", fg="blue")
    l1 = Label(text='Для начала игры\nвведите "o" или "x" в любое\nполе и нажмите Enter', font=(
        "Arial Black", 11), bg="lightgreen", fg="blue")
elif rand == 1:
    l = Label(text='Игру начинает игрок Б', font=(
        "Arial Black", 10), bg="lightgreen", fg="blue")
    l1 = Label(text='Для начала игры\nвведите "o" или "x" в любое\nполе и нажмите Enter', font=(
        "Arial Black", 11), bg="lightgreen", fg="blue")
l.grid(row=3, column=4)
l1.grid(row=4, column=4)

o = str('o')
x = str('x')
l2 = Label()
l3 = Label()
l4 = Label()
get1, get2, get3, get4, get5, get6, get7, get8, get9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
v5 = StringVar()
v6 = StringVar()
v7 = StringVar()
v8 = StringVar()
v9 = StringVar()

e1 = Entry(textvariable=v1, width=4, justify=CENTER,
           font=font.Font(family="Arial Black", size=10))
e2 = Entry(textvariable=v2, width=4, justify=CENTER,
           font=font.Font(family="Arial Black", size=10))
e3 = Entry(textvariable=v3, width=4, justify=CENTER,
           font=font.Font(family="Arial Black", size=10))
e4 = Entry(textvariable=v4, width=4, justify=CENTER,
           font=font.Font(family="Arial Black", size=10))
e5 = Entry(textvariable=v5, width=4, justify=CENTER,
           font=font.Font(family="Arial Black", size=10))
e6 = Entry(textvariable=v6, width=4, justify=CENTER,
           font=font.Font(family="Arial Black", size=10))
e7 = Entry(textvariable=v7, width=4, justify=CENTER,
           font=font.Font(family="Arial Black", size=10))
e8 = Entry(textvariable=v8, width=4, justify=CENTER,
           font=font.Font(family="Arial Black", size=10))
e9 = Entry(textvariable=v9, width=4, justify=CENTER,
           font=font.Font(family="Arial Black", size=10))


def check_mistake(_get, _e):
    global rand
    if _get == o or _get == x:
        if rand == 0:
            l2 = Label(text='Ход игрока Б',
                       font=("Arial Black", 11), bg="lightblue", fg="blue")
            rand = 1
            l2.grid(row=1, column=4)
        elif rand == 1:
            l2 = Label(text='Ход игрока А',
                       font=("Arial Black", 11), bg="lightblue", fg="blue")
            rand = 0
            l2.grid(row=1, column=4)
    else:
        mb.showerror("Ошибка", "Должно быть введено 'o' или 'x'")
        _e.delete(0, END)
    return rand


def winner():
    if rand == 1:
        l3 = Label(text='Победитель - игрок А',
                   font=("Arial Black", 12), bg="red", fg="lightblue")
        l3.grid(row=2, column=4)
    elif rand == 0:
        l3 = Label(text='Победитель - игрок Б',
                   font=("Arial Black", 12), bg="red", fg="lightblue")
        l3.grid(row=2, column=4)


def standoff():
    if (get1 == o or get1 == x) and (get2 == o or get2 == x) and (get3 == o or get3 == x) and (get4 == o or get4 == x) and (get5 == o or get5 == x) and (get6 == o or get6 == x) and (get7 == o or get7 == x) and (get8 == o or get8 == x) and (get9 == o or get9 == x):
        l4 = Label(text='Ничья',
                   font=("Arial Black", 12), bg="red", fg="lightblue")
        l4.grid(row=5, column=4)


def enter1(event):
    global get1
    get1 = v1.get()
    check_mistake(get1, e1)
    standoff()
    if get1 == o and get2 == o and get3 == o or get1 == x and get2 == x and get3 == x:
        e1.configure(background="green")
        e2.configure(background="green")
        e3.configure(background="green")
        winner()
    elif get1 == o and get4 == o and get7 == o or get1 == x and get4 == x and get7 == x:
        e1.configure(background="green")
        e4.configure(background="green")
        e7.configure(background="green")
        winner()
    elif get1 == o and get5 == o and get9 == o or get1 == x and get4 == x and get7 == x:
        e1.configure(background="green")
        e5.configure(background="green")
        e9.configure(background="green")
        winner()


def enter2(event):
    global get2
    get2 = v2.get()
    check_mistake(get2, e2)
    standoff()
    if get2 == o and get1 == o and get3 == o or get2 == x and get1 == x and get3 == x:
        e2.configure(background="green")
        e1.configure(background="green")
        e3.configure(background="green")
        winner()
    elif get2 == o and get5 == o and get8 == o or get2 == x and get5 == x and get8 == x:
        e2.configure(background="green")
        e5.configure(background="green")
        e8.configure(background="green")
        winner()


def enter3(event):
    global get3
    get3 = v3.get()
    check_mistake(get3, e3)
    standoff()
    if get3 == o and get2 == o and get1 == o or get3 == x and get2 == x and get1 == x:
        e3.enter3.configure(background="green")
        e2.configure(background="green")
        e1.configure(background="green")
        winner()
    elif get3 == o and get6 == o and get9 == o or get3 == x and get6 == x and get9 == x:
        e3.configure(background="green")
        e6.configure(background="green")
        e9.configure(background="green")
        winner()
    elif get3 == o and get5 == o and get7 == o or get3 == x and get5 == x and get7 == x:
        e3.configure(background="green")
        e5.configure(background="green")
        e7.configure(background="green")
        winner()


def enter4(event):
    global get4
    get4 = v4.get()
    check_mistake(get4, e4)
    standoff()
    if get4 == o and get1 == o and get7 == o or get4 == x and get1 == x and get7 == x:
        e4.configure(background="green")
        e1.configure(background="green")
        e7.configure(background="green")
        winner()
    elif get4 == o and get5 == o and get6 == o or get4 == x and get5 == x and get6 == x:
        e4.configure(background="green")
        e5.configure(background="green")
        e6.configure(background="green")
        winner()


def enter5(event):
    global get5
    get5 = v5.get()
    check_mistake(get5, e5)
    standoff()
    if get5 == o and get4 == o and get6 == o or get5 == x and get4 == x and get6 == x:
        e5.configure(background="green")
        e4.configure(background="green")
        e6.configure(background="green")
        winner()
    elif get5 == o and get2 == o and get8 == o or get5 == x and get2 == x and get8 == x:
        e5.configure(background="green")
        e2.configure(background="green")
        e8.configure(background="green")
        winner()


def enter6(event):
    global get6
    get6 = v6.get()
    check_mistake(get6, e6)
    standoff()
    if get6 == o and get5 == o and get4 == o or get6 == x and get5 == x and get4 == x:
        e6.configure(background="green")
        e5.configure(background="green")
        e4.configure(background="green")
        winner()
    elif get6 == o and get3 == o and get9 == o or get6 == x and get3 == x and get9 == x:
        e6.configure(background="green")
        e3.configure(background="green")
        e9.configure(background="green")
        winner()


def enter7(event):
    global get7
    get7 = v7.get()
    check_mistake(get7, e7)
    standoff()
    if get7 == o and get4 == o and get1 == o or get7 == x and get4 == x and get1 == x:
        e7.configure(background="green")
        e4.configure(background="green")
        e1.configure(background="green")
        winner()
    elif get7 == o and get8 == o and get9 == o or get7 == x and get8 == x and get9 == x:
        e7.configure(background="green")
        e8.configure(background="green")
        e9.configure(background="green")
        winner()
    elif get7 == o and get5 == o and get3 == o or get7 == x and get5 == x and get3 == x:
        e7.configure(background="green")
        e5.configure(background="green")
        e3.configure(background="green")
        winner()


def enter8(event):
    global get8
    get8 = v8.get()
    check_mistake(get8, e8)
    standoff()
    if get8 == o and get5 == o and get2 == o or get8 == x and get5 == x and get2 == x:
        e8.configure(background="green")
        e5.configure(background="green")
        e2.configure(background="green")
        winner()
    elif get8 == o and get7 == o and get9 == o or get8 == x and get7 == x and get9 == x:
        e8.configure(background="green")
        e7.configure(background="green")
        e9.configure(background="green")
        winner()


def enter9(event):
    global get9
    get9 = v9.get()
    check_mistake(get9, e9)
    standoff()
    if get9 == o and get5 == o and get1 == o or get9 == x and get5 == x and get1 == x:
        e9.configure(background="green")
        e5.configure(background="green")
        e1.configure(background="green")
        winner()
    elif get9 == o and get8 == o and get7 == o or get9 == x and get8 == x and get7 == x:
        e9.configure(background="green")
        e8.configure(background="green")
        e7.configure(background="green")
        winner()
    elif get9 == o and get6 == o and get3 == o or get9 == x and get6 == x and get3 == x:
        e9.configure(background="green")
        e6.configure(background="green")
        e3.configure(background="green")
        winner()


e1.bind('<Return>', enter1)
e2.bind('<Return>', enter2)
e3.bind('<Return>', enter3)
e4.bind('<Return>', enter4)
e5.bind('<Return>', enter5)
e6.bind('<Return>', enter6)
e7.bind('<Return>', enter7)
e8.bind('<Return>', enter8)
e9.bind('<Return>', enter9)

e1.grid(row=1, column=1)
e2.grid(row=1, column=2)
e3.grid(row=1, column=3)
e4.grid(row=2, column=1)
e5.grid(row=2, column=2)
e6.grid(row=2, column=3)
e7.grid(row=3, column=1)
e8.grid(row=3, column=2)
e9.grid(row=3, column=3)

root.mainloop()
