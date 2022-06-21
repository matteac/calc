from curses import BUTTON1_CLICKED, window
from os import O_WRONLY
from tkinter import *
from funcs import *


def genBtns(win, io):
    btn1 = Button(win, text=1, command=lambda: append(io, 1))
    btn1.grid(column=0, row=1)

    btn2 = Button(win, text=2, command=lambda: append(io, 2))
    btn2.grid(column=1, row=1)

    btn3 = Button(win, text=3, command=lambda: append(io, 3))
    btn3.grid(column=2, row=1)


    deleteBtn = Button(win, text="DEL", command=lambda: delOne(io))
    deleteBtn.grid(column=3, row=1)

    acBtn = Button(win, text="AC", command=lambda: ac(io))
    acBtn.grid(column=4, row=1)

    #second
    btn4 = Button(win, text=4, command=lambda: append(io, 4))
    btn4.grid(column=0, row=2)

    btn5 = Button(win, text=5, command=lambda: append(io, 5))
    btn5.grid(column=1, row=2)

    btn6 = Button(win, text=6, command=lambda: append(io, 6))
    btn6.grid(column=2, row=2)

    minus = Button(win, text="-", command=lambda: operation(io, "-"))
    minus.grid(column=3, row=2)

    plus = Button(win, text="+", command=lambda: operation(io, "+"))
    plus.grid(column=4, row=2)

    #third
    btn7 = Button(win, text=7, command=lambda: append(io, 7))
    btn7.grid(column=0, row=3)

    btn8 = Button(win, text=8, command=lambda: append(io, 8))
    btn8.grid(column=1, row=3)

    btn9 = Button(win, text=9, command=lambda: append(io, 9))
    btn9.grid(column=2, row=3)

    multiply = Button(win, text="*", command=lambda: operation(io, "*"))
    multiply.grid(column=3, row=3)

    divide = Button(win, text="/", command=lambda: operation(io, "/"))
    divide.grid(column=4, row=3)

    #fourth
    btn0 = Button(win, text=0, command=lambda: append(io, 0))
    btn0.grid(column=1, row=4)

    dot = Button(win, text=".", command=lambda: append(io, "."))
    dot.grid(column=2, row=4)

    ansBtn = Button(win, text="ANS", command=lambda: showAns(io))
    ansBtn.grid(column=3, row=4)

    equal = Button(win, text="=", command=lambda: Eval(io))
    equal.grid(column=4, row=4)

