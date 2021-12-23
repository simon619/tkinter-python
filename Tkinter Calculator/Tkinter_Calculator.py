from tkinter import *
import math

root = Tk()
root.configure(background='black')
root.title("Tkinter Calculator")
root.iconbitmap("Radiation.ico")

e = Entry(root, width=40, borderwidth=2)
e.grid(row=0, column=0, padx=10, pady=20, columnspan=3)


def button_Click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_Clear():
    e.delete(0, END)


def button_Add():
    n = float(e.get())
    global first_number
    first_number = n
    global math
    math = "Addition"
    e.delete(0, END)


def button_Sub():
    n = float(e.get())
    global first_number
    first_number = n
    global math
    math = "Subtraction"
    e.delete(0, END)


def button_Mul():
    n = float(e.get())
    global first_number
    first_number = n
    global math
    math = "Multiplication"
    e.delete(0, END)


def button_Div():
    n = float(e.get())
    global first_number
    first_number = n
    global math
    math = "Division"
    e.delete(0, END)


def button_Anysq():
    n = e.get()
    global first_number
    first_number = float(n)
    global math
    math = "Square"
    e.delete(0, END)


def button_Equal():
    second_number = float(e.get())
    e.delete(0, END)
    if math == "Addition":
        e.insert(0, first_number + second_number)

    elif math == "Subtraction":
        e.insert(0, first_number - second_number)

    elif math == "Multiplication":
        e.insert(0, first_number * second_number)

    elif math == "Division":
        e.insert(0, first_number / second_number)

    elif math == "Square":
        e.insert(0, first_number ** second_number)


def button_Sq():
    number = float(e.get())
    e.insert(0, number ** 2)


def button_Sqrt():
    number = float(e.get())
    number = math.sqrt(number)
    e.insert(0, number)


def button_Operation(String):
    number = float(e.get())
    if String == 'sin':
        e.insert(0, math.sin(number))
    elif String == 'cos':
        e.insert(0, math.cos(number))
    elif String == 'cos':
        e.insert(0, math.tan(number))
    elif String == 'log':
        e.insert(0, math.log(number))
    elif String == 'e':
        e.insert(0, math.exp(number))
    elif String == 'ln':
        e.insert(0, math.ln(number))


button7 = Button(root, text="7", padx=35, pady=20, command=lambda: button_Click(7))
button8 = Button(root, text="8", padx=36, pady=20, command=lambda: button_Click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_Click(9))
button4 = Button(root, text="4", padx=35, pady=20, command=lambda: button_Click(4))
button5 = Button(root, text="5", padx=36, pady=20, command=lambda: button_Click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_Click(6))
button1 = Button(root, text="1", padx=35, pady=20, command=lambda: button_Click(1))
button2 = Button(root, text="2", padx=36, pady=20, command=lambda: button_Click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_Click(3))
button0 = Button(root, text="0", padx=35, pady=20, command=lambda: button_Click(0))
buttonfloatingpoint = Button(root, text=".", padx=45, pady=20, command=lambda: button_Click('.'))
buttonclear = Button(root, text="CE", padx=36, pady=20, command=button_Clear)
buttonadd = Button(root, text="+", padx=35.5, pady=20, command=button_Add)
buttonsub = Button(root, text="-", padx=37, pady=20, command=button_Sub)
buttonmul = Button(root, text="*", padx=37, pady=20, command=button_Mul)
buttondiv = Button(root, text="/", padx=37, pady=20, command=button_Div)
buttonsq = Button(root, text="x^2", padx=36, pady=20, command=button_Sq)
buttonsqrt = Button(root, text="root", padx=35, pady=20, command=button_Sqrt)
buttonanysq = Button(root, text="x^n", padx=35.5, pady=20, command=button_Anysq)
buttonsin = Button(root, text="sin", padx=37, pady=20, command=lambda: button_Operation("sin"))
buttoncos = Button(root, text="cos", padx=35, pady=20, command=lambda: button_Operation("cos"))
buttontan = Button(root, text="tan", padx=35, pady=20, command=lambda: button_Operation("tan"))
buttonlog = Button(root, text="log", padx=35, pady=20, command=lambda: button_Operation("log"))
buttone = Button(root, text="e", padx=40, pady=20, command=lambda: button_Operation("e"))
buttonln = Button(root, text="ln", padx=42, pady=20, command=lambda: button_Operation("ln"))
buttonequal = Button(root, text="=", padx=35, pady=20, command=button_Equal)
quitbutton = Button(root, text="Exit", padx=27, pady=20, bg="red", command=root.quit)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button0.grid(row=4, column=0)
buttonfloatingpoint.grid(row=4, column=4)
buttonadd.grid(row=1, column=3)
buttonsub.grid(row=2, column=3)
buttonmul.grid(row=3, column=3)
buttondiv.grid(row=4, column=3)
buttonsq.grid(row=1, column=4)
buttonsqrt.grid(row=2, column=4)
buttonanysq.grid(row=3, column=4)
buttonsin.grid(row=1, column=5)
buttoncos.grid(row=2, column=5)
buttontan.grid(row=3, column=5)
buttonlog.grid(row=4, column=5)
buttone.grid(row=5, column=5)
buttonln.grid(row=5, column=4)
buttonequal.grid(row=4, column=1)
buttonclear.grid(row=4, column=2)
quitbutton.grid(row=5, column=0)

root.mainloop()
