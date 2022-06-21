from btns import *
from tkinter import *

def main():
    window = Tk()

    window.title("Calc")
    window.configure(width=600, height = 600)


    rell1 = Label(window, text="", font=18)
    rell1.grid(column=0, row=0)

    IO = Entry(window, width=22, font=12)
    IO.place(x=0, y=0)


    genBtns(window, IO)


    window.mainloop()


if __name__ == "__main__":
    main()