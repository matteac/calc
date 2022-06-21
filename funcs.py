from tkinter import messagebox


ans = {
    "ans": ""
}




def showAns(io):
    io.delete(0, len(io.get()))
    io.insert(0, ans["ans"])

def ac(io):
    io.delete(0, len(io.get()))

def delOne(io):
    io.delete(len(io.get())-1, len(io.get()))

def append(io, i):
    io.insert(len(io.get()), i)

def operation(io, op):
    opList = ["+", "-", "*", "/"]
    actualText = io.get()
    textLength = len(actualText)
    if actualText[textLength-1] not in opList:
        io.insert(textLength, op)
    else:
        print("Error")

def Eval(io):
    try:
        res = eval(io.get())
        ans["ans"] = res
        io.delete(0, len(io.get()))
        io.insert(0, res)
    except (SyntaxError, AttributeError):
        messagebox.showerror("Error", "Syntax Error")
        io.delete(0, len(io.get()))
        io.insert(0, "")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot Divide by 0")
        io.delete(0, len(io.get()))
        io.insert(0, "")