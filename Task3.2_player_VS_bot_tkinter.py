# Создайте программу для игры в ""Крестики-нолики"".
# человек против бота
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
    l = Label(text='Ваш ход', font=(
        "Arial Black", 10), bg="lightgreen", fg="blue")
    l1 = Label(text='Для выполнения хода\nвведите "o" в любое свободное поле\n и нажмите Enter', font=(
        "Arial Black", 11), bg="lightgreen", fg="blue")
elif rand == 1:
    l = Label(text='Первый ходит бот', font=(
        "Arial Black", 10), bg="lightgreen", fg="blue")
    l1 = Label(text='Для выполнения хода\nвведите "o" в любое свободное поле\n и нажмите Enter', font=(
        "Arial Black", 11), bg="lightgreen", fg="blue")
l.grid(row=3, column=4)
l1.grid(row=4, column=4)

a1, a2, a3, a4, a5, a6, a7, a8, a9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
get1, get2, get3, get4, get5, get6, get7, get8, get9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
o = str('o')
x = str('x')
l2 = Label()
l3 = Label()
l4 = Label()
c, n, d = 0, 0, 0

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
    if _get == o:
        if rand == 1:
            l2 = Label(text='Ходит бот',
                       font=("Arial Black", 11), bg="lightblue", fg="blue")
            rand = 1
            l2.grid(row=1, column=4)
        elif rand == 0:
            l2 = Label(text='Ваш ход',
                       font=("Arial Black", 11), bg="lightblue", fg="blue")
            rand = 0
            l2.grid(row=1, column=4)
    else:
        mb.showerror("Ошибка", "Должно быть введено 'o'")
        _e.delete(0, END)
    return rand


def winner():
    if a1 == x and a2 == x and a3 == x or a4 == x and a5 == x and a6 == x or a7 == x and a8 == x and a9 == x or a1 == x and a4 == x and a7 == x or a2 == x and a5 == x and a8 == x or a3 == x and a6 == x and a9 == x or a1 == x and a5 == x and a9 == x or a7 == x and a5 == x and a3 == x:
        l3 = Label(text='Вы проиграли',
                   font=("Arial Black", 12), bg="red", fg="lightblue")
        l3.grid(row=2, column=4)
    else:
        l3 = Label(text='Вы - Победитель',
                   font=("Arial Black", 12), bg="red", fg="lightblue")
        l3.grid(row=2, column=4)


def standoff():
    if (get1 == o or a1 == x) and (get2 == o or a2 == x) and (get3 == o or a3 == x) and (get4 == o or a4 == x) and (get5 == o or a5 == x) and (get6 == o or a6 == x) and (get7 == o or a7 == x) and (get8 == o or a8 == x) and (get9 == o or a9 == x):
        l4 = Label(text='Ничья',
                   font=("Arial Black", 12), bg="red", fg="lightblue")
        l4.grid(row=5, column=4)


def color1():
    if get1 == o and get2 == o and get3 == o or a1 == x and a2 == x and a3 == x:
        e1.configure(background="green")
        e2.configure(background="green")
        e3.configure(background="green")
        winner()
    elif get1 == o and get4 == o and get7 == o or a1 == x and a4 == x and a7 == x:
        e1.configure(background="green")
        e4.configure(background="green")
        e7.configure(background="green")
        winner()
    elif get1 == o and get5 == o and get9 == o or a1 == x and a5 == x and a9 == x:
        e1.configure(background="green")
        e5.configure(background="green")
        e9.configure(background="green")
        winner()


def color2():
    if get2 == o and get1 == o and get3 == o or a2 == x and a1 == x and a3 == x:
        e2.configure(background="green")
        e1.configure(background="green")
        e3.configure(background="green")
        winner()
    elif get2 == o and get5 == o and get8 == o or a2 == x and a5 == x and a8 == x:
        e2.configure(background="green")
        e5.configure(background="green")
        e8.configure(background="green")
        winner()


def color3():
    if get3 == o and get2 == o and get1 == o or a3 == x and a2 == x and a1 == x:
        e3.enter3.configure(background="green")
        e2.configure(background="green")
        e1.configure(background="green")
        winner()
    elif get3 == o and get6 == o and get9 == o or a3 == x and a6 == x and a9 == x:
        e3.configure(background="green")
        e6.configure(background="green")
        e9.configure(background="green")
        winner()
    elif get3 == o and get5 == o and get7 == o or a3 == x and a5 == x and a7 == x:
        e3.configure(background="green")
        e5.configure(background="green")
        e7.configure(background="green")
        winner()


def color4():
    if get4 == o and get1 == o and get7 == o or a4 == x and a1 == x and a7 == x:
        e4.configure(background="green")
        e1.configure(background="green")
        e7.configure(background="green")
        winner()
    elif get4 == o and get5 == o and get6 == o or a4 == x and a5 == x and a6 == x:
        e4.configure(background="green")
        e5.configure(background="green")
        e6.configure(background="green")
        winner()


def color5():
    if get5 == o and get4 == o and get6 == o or a5 == x and a4 == x and a6 == x:
        e5.configure(background="green")
        e4.configure(background="green")
        e6.configure(background="green")
        winner()
    elif get5 == o and get2 == o and get8 == o or a5 == x and a2 == x and a8 == x:
        e5.configure(background="green")
        e2.configure(background="green")
        e8.configure(background="green")
        winner()


def color6():
    if get6 == o and get5 == o and get4 == o or a6 == x and a5 == x and a4 == x:
        e6.configure(background="green")
        e5.configure(background="green")
        e4.configure(background="green")
        winner()
    elif get6 == o and get3 == o and get9 == o or a6 == x and a3 == x and a9 == x:
        e6.configure(background="green")
        e3.configure(background="green")
        e9.configure(background="green")
        winner()


def color7():
    if get7 == o and get4 == o and get1 == o or a7 == x and a4 == x and a1 == x:
        e7.configure(background="green")
        e4.configure(background="green")
        e1.configure(background="green")
        winner()
    elif get7 == o and get8 == o and get9 == o or a7 == x and a8 == x and a9 == x:
        e7.configure(background="green")
        e8.configure(background="green")
        e9.configure(background="green")
        winner()
    elif get7 == o and get5 == o and get3 == o or a7 == x and a5 == x and a3 == x:
        e7.configure(background="green")
        e5.configure(background="green")
        e3.configure(background="green")
        winner()


def color8():
    if get8 == o and get5 == o and get2 == o or a8 == x and a5 == x and a2 == x:
        e8.configure(background="green")
        e5.configure(background="green")
        e2.configure(background="green")
        winner()
    elif get8 == o and get7 == o and get9 == o or a8 == x and a7 == x and a9 == x:
        e8.configure(background="green")
        e7.configure(background="green")
        e9.configure(background="green")
        winner()


def color9():
    if get9 == o and get5 == o and get1 == o or a9 == x and a5 == x and a1 == x:
        e9.configure(background="green")
        e5.configure(background="green")
        e1.configure(background="green")
        winner()
    elif get9 == o and get8 == o and get7 == o or a9 == x and a8 == x and a7 == x:
        e9.configure(background="green")
        e8.configure(background="green")
        e7.configure(background="green")
        winner()
    elif get9 == o and get6 == o and get3 == o or a9 == x and a6 == x and a3 == x:
        e9.configure(background="green")
        e6.configure(background="green")
        e3.configure(background="green")
        winner()


def check_ooo():  # проверяет три'o' подряд
    global p
    p = 0
    if get1 == o and get2 == o and get3 == o:
        color1()
        p = 1
    if get1 == o and get4 == o and get7 == o:
        color1()
        p = 1
    if get1 == o and get5 == o and get9 == o:
        color1()
        p = 1
    if get2 == o and get5 == o and get8 == o:
        color2()
        p = 1
    if get3 == o and get6 == o and get9 == o:
        color3()
        p = 1
    if get3 == o and get5 == o and get7 == o:
        color3()
        p = 1
    if get4 == o and get5 == o and get6 == o:
        color4()
        p = 1
    if get7 == o and get8 == o and get9 == o:
        color7()
        p = 1


def add_third_x():  # ставит 'x' перед двумя подряд "o", 'o'
    global e, f, d, c, b, t, a1, a2, a3, a4, a5, a6, a7, a8, a9, get1, get2, get3, get4, get5, get6, get7, get8, get9
    f = 0
    e = 0
    if get1 == o and get2 == o or get6 == o and get9 == o or get7 == o and get5 == o:
        if a3 != x:
            e = e + 1
            e3.insert(INSERT, "x")
            a3 = x
            color3()
            f = 1
    if get1 == o and get4 == o or get9 == o and get8 == o or get3 == o and get5 == o:
        if a7 != x and e == 0:
            e = e + 1
            e7.insert(INSERT, "x")
            a7 = x
            color7()
            f = 1
    if get2 == o and get3 == o or get7 == o and get4 == o or get9 == o and get5 == o:
        if a1 != x and e == 0:
            e = e + 1
            e1.insert(INSERT, "x")
            a1 = x
            color1()
            f = 1
    if get3 == o and get6 == o or get7 == o and get8 == o or get1 == o and get5 == o:
        if a9 != x and e == 0:
            e = e + 1
            e9.insert(INSERT, "x")
            a9 = x
            color9()
            f = 1
    if get8 == o and get5 == o or get1 == o and get3 == o:
        if a2 != x and e == 0:
            e = e + 1
            e2.insert(INSERT, "x")
            a2 = x
            color2()
            f = 1
    if get2 == o and get5 == o or get7 == o and get9 == o:
        if a8 != x and e == 0:
            e = e + 1
            e8.insert(INSERT, "x")
            a8 = x
            color8()
            f = 1
    if get4 == o and get5 == o or get3 == o and get9 == o:
        if a6 != x and e == 0:
            e = e + 1
            e6.insert(INSERT, "x")
            a6 = x
            color6()
            f = 1
    if get5 == o and get6 == o or get1 == o and get7 == o:
        if a4 != x and e == 0:
            e = e + 1
            e4.insert(INSERT, "x")
            a4 = x
            color4()
            f = 1


def bot_first_move():
    global d, c, b, t, a1, a2, a3, a4, a5, a6, a7, a8, a9, get1, get2, get3, get4, get5, get6, get7, get8, get9
    list2 = [get1, get2, get3, get4, get5, get6, get7, get8, get9]
    list1 = [a1, a2, a3, a4, a5, a6, a7, a8, a9]
    t = 0
    if get1 == o:
        if a2 != x:
            c = c + 1
            bot1()
            if b == 0 and get2 != o:
                e2.insert(INSERT, "x")
                a2 = x
                color2()
                t = 1
    if get2 == o:
        if a3 != x:
            c = c + 1
            bot1()
            if b == 0 and get3 != o:
                e3.insert(INSERT, "x")
                a3 = x
                color3()
                t = 1
    if get3 == o:
        if a6 != x:
            c = c + 1
            bot1()
            if b == 0 and get6 != o:
                e6.insert(INSERT, "x")
                a6 = x
                color6()
                t = 1
    if get4 == o:
        if a1 != x:
            c = c + 1
            bot1()
            if b == 0 and get1 != o:
                e1.insert(INSERT, "x")
                a1 = x
                color1()
                t = 1
    if get6 == o:
        if a9 != x:
            c = c + 1
            bot1()
            if b == 0 and get9 != o:
                e9.insert(INSERT, "x")
                a9 = x
                color9()
                t = 1
    if get7 == o:
        if a4 != x:
            c = c + 1
            bot1()
            if b == 0 and get4 != o:
                e4.insert(INSERT, "x")
                a4 = x
                color4()
                t = 1
    if get8 == o:
        if a7 != x:
            c = c + 1
            bot1()
            if b == 0 and get7 != o:
                e7.insert(INSERT, "x")
                a7 = x
                color7()
                t = 1
    if get9 == o:
        if a8 != x:
            c = c + 1
            bot1()
            if b == 0 and get8 != o:
                e8.insert(INSERT, "x")
                a8 = x
                color8()
                t = 1
    if get5 == o:
        # if a8 != x:
        c = c + 1
        t = 1
        bot1()
        if b == 0:  # :
            # e8.insert(INSERT, "x")
            # a8 = x
            color8()
    if c == 4 and b != 1:
        for i in range(len(list1)):
            if list2[i] == 0 and list1[i] == 0:
                if i == 0:
                    e1.insert(INSERT, "x")
                    a1 = x
                if i == 1:
                    e2.insert(INSERT, "x")
                    a2 = x
                if i == 2:
                    e3.insert(INSERT, "x")
                    a3 = x
                if i == 3:
                    e4.insert(INSERT, "x")
                    a4 = x
                if i == 4:
                    e5.insert(INSERT, "x")
                    a5 = x
                if i == 5:
                    e6.insert(INSERT, "x")
                    a6 = x
                if i == 6:
                    e7.insert(INSERT, "x")
                    a7 = x
                if i == 7:
                    e8.insert(INSERT, "x")
                    a8 = x
                if i == 8:
                    e9.insert(INSERT, "x")
                    a9 = x
            standoff()


def man_first_move():
    global d, c, b, t, a1, a2, a3, a4, a5, a6, a7, a8, a9, get1, get2, get3, get4, get5, get6, get7, get8, get9
    list2 = [get1, get2, get3, get4, get5, get6, get7, get8, get9]
    list1 = [a1, a2, a3, a4, a5, a6, a7, a8, a9]
    t = 0
    c = 0
    if get1 == o:
        if get2 != o and a2 != x:
            c = c + 1
            e2.insert(INSERT, "x")
            a2 = x
            color2()
            t = 1
    if get2 == o:
        if get3 != o and a3 != x and c == 0:
            c = c + 1
            e3.insert(INSERT, "x")
            a3 = x
            color3()
            t = 1
    if get3 == o:
        if get6 != o and a6 != x and c == 0:
            c = c + 1
            e6.insert(INSERT, "x")
            a6 = x
            color6()
            t = 1
    if get4 == o:
        if get1 != o and a1 != x and c == 0:
            c = c + 1
            e1.insert(INSERT, "x")
            a1 = x
            color1()
            t = 1
    if get6 == o:
        if get9 != o and a9 != x and c == 0:
            c = c + 1
            e9.insert(INSERT, "x")
            a9 = x
            color9()
            t = 1
    if get7 == o:
        if get4 != o and a4 != x and c == 0:
            c = c + 1
            e4.insert(INSERT, "x")
            a4 = x
            color4()
            t = 1
    if get8 == o:
        if get7 != o and a7 != x and c == 0:
            c = c + 1
            e7.insert(INSERT, "x")
            a7 = x
            color7()
            t = 1
    if get9 == o:
        if get8 != o and a8 != x and c == 0:
            c = c + 1
            e8.insert(INSERT, "x")
            a8 = x
            color8()
            t = 1
    if c == 4 and t != 1:
        for i in range(len(list1)):
            if list2[i] == 0 and list1[i] == 0:
                if i == 0:
                    e1.insert(INSERT, "x")
                    a1 = x
                if i == 1:
                    e2.insert(INSERT, "x")
                    a2 = x
                if i == 2:
                    e3.insert(INSERT, "x")
                    a3 = x
                if i == 3:
                    e4.insert(INSERT, "x")
                    a4 = x
                if i == 4:
                    e5.insert(INSERT, "x")
                    a5 = x
                if i == 5:
                    e6.insert(INSERT, "x")
                    a6 = x
                if i == 6:
                    e7.insert(INSERT, "x")
                    a7 = x
                if i == 7:
                    e8.insert(INSERT, "x")
                    a8 = x
                if i == 8:
                    e9.insert(INSERT, "x")
                    a9 = x

            standoff()


def bot1():  # ставит последний х в линии проходящей через а5
    global b, a1, a2, a3, a4, a5, a6, a7, a8, a9
    b = 0
    if a1 == x and get9 != o:
        e9.insert(INSERT, "x")
        a9 = x
        color1()
        b = 1
    elif a9 == x and get1 != o:
        e1.insert(INSERT, "x")
        a1 = x
        color9()
        b = 1
    elif a3 == x and get7 != o:
        e7.insert(INSERT, "x")
        a7 = x
        color3()
        b = 1
    elif a7 == x and get3 != o:
        e3.insert(INSERT, "x")
        a3 = x
        color7()
        b = 1
    elif a2 == x and get8 != o:
        e8.insert(INSERT, "x")
        a8 = x
        color2()
        b = 1
    elif a8 == x and get2 != o:
        e2.insert(INSERT, "x")
        a2 = x
        color8()
        b = 1
    elif a4 == x and get6 != o:
        e6.insert(INSERT, "x")
        a6 = x
        color4()
        b = 1
    elif a6 == x and get4 != o:
        e4.insert(INSERT, "x")
        a4 = x
        color6()
        b = 1


def bot2():  # ставит последний 'x' при get5 == o
    global d, a1, a2, a3, a4, a5, a6, a7, a8, a9, get1, get2, get3, get4, get5, get6, get7, get8, get9
    d = 0
    if a1 == x and a4 == x and a7 != x and get7 != o:
        e7.insert(INSERT, "x")
        a7 = x
        color1()
        d = 1
    if a1 == x and a2 == x and a3 != x and get3 != o:
        e3.insert(INSERT, "x")
        a3 = x
        color1()
        d = 1
    if a1 == x and a3 == x and a2 != x and get2 != o:
        e2.insert(INSERT, "x")
        a2 = x
        color1()
        d = 1
    if a1 == x and a7 == x and a4 != x and get4 != o:
        e4.insert(INSERT, "x")
        a4 = x
        color1()
        d = 1
    if a1 == 7 and a8 == x and a9 != x and get9 != o:
        e9.insert(INSERT, "x")
        a9 = x
        color7()
        d = 1
    if a9 == x and a8 == x and a7 != x and get7 != o:
        e7.insert(INSERT, "x")
        a7 = x
        color9()
        d = 1
    if a9 == x and a7 == x and a8 != x and get8 != o:
        e8.insert(INSERT, "x")
        a8 = x
        color9()
        d = 1
    if a9 == x and a6 == x and a3 != x and get3 != o:
        e3.insert(INSERT, "x")
        a3 = x
        color9()
        d = 1
    if a3 == x and a9 == x and a6 != x and get6 != o:
        e6.insert(INSERT, "x")
        a6 = x
        color3()
        d = 1
    if a3 == x and a6 == x and a9 != x and get9 != o:
        e9.insert(INSERT, "x")
        a9 = x
        color3()
        d = 1


def bot():
    global a1, a2, a3, a4, a5, a6, a7, a8, a9, c, n, d, b, t, p
    global get1, get2, get3, get4, get5, get6, get7, get8, get9
    p = 0
    if rand == 0:
        list2 = [get1, get2, get3, get4, get5, get6, get7, get8, get9]
        list1 = [a1, a2, a3, a4, a5, a6, a7, a8, a9]
        if get5 != o:
            if a5 != x:
                e5.insert(INSERT, "x")
                a5 = x
            else:
                bot1()
                if b != 1:
                    add_third_x()
                    if f != 1:
                        man_first_move()

        elif get5 == o:
            if a1 != x:
                e1.insert(INSERT, "x")
                a1 = x
            check_ooo()
            if p != 1:
                bot2()
                if d != 1:
                    add_third_x()
                    if f != 1:
                        man_first_move()

    if rand == 1:
        bot_first_move()


def enter1(event):
    global get1
    get1 = v1.get()
    check_mistake(get1, e1)
    standoff()
    bot()


def enter2(event):
    global get2
    get2 = v2.get()
    check_mistake(get2, e2)
    standoff()
    bot()


def enter3(event):
    global get3
    get3 = v3.get()
    check_mistake(get3, e3)
    standoff()
    bot()


def enter4(event):
    global get4
    get4 = v4.get()
    check_mistake(get4, e4)
    standoff()
    bot()


def enter5(event):
    global get5
    get5 = v5.get()
    check_mistake(get5, e5)
    standoff()
    bot()


def enter6(event):
    global get6
    get6 = v6.get()
    check_mistake(get6, e6)
    standoff()
    bot()


def enter7(event):
    global get7
    get7 = v7.get()
    check_mistake(get7, e7)
    standoff()
    bot()


def enter8(event):
    global get8
    get8 = v8.get()
    check_mistake(get8, e8)
    standoff()
    bot()


def enter9(event):
    global get9
    get9 = v9.get()
    check_mistake(get9, e9)
    standoff()
    bot()


if rand == 1:
    if a5 != x:
        e5.insert(INSERT, "x")
        a5 = x
    bot()

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
