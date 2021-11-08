from tkinter import *

pad_x = 15
pad_y = 10
border_width = 3
values_width = 20
entry_width = 20
history_width = 40
history_height = 60


def number_click(entry):
    lenght = len(inputBox.get())
    inputBox.insert(lenght, entry)


def clear_click(event):
    inputBox.delete(0, len(inputBox.get()))

def clear():
    inputBox.delete(0, len(inputBox.get()))

def delete_click(event):
    inputBox.delete(len(inputBox.get()) - 1, len(inputBox.get()))


def set_Decimal():
    clear()

    button_A["state"] = 'disabled'
    button_B["state"] = 'disabled'
    button_C["state"] = 'disabled'
    button_D["state"] = 'disabled'
    button_E["state"] = 'disabled'
    button_F["state"] = 'disabled'

    button_0["state"] = 'normal'
    button_1["state"] = 'normal'
    button_2["state"] = 'normal'
    button_3["state"] = 'normal'
    button_4["state"] = 'normal'
    button_5["state"] = 'normal'
    button_6["state"] = 'normal'
    button_7["state"] = 'normal'
    button_8["state"] = 'normal'
    button_9["state"] = 'normal'


def set_Hex():
    clear()

    button_A["state"] = 'normal'
    button_B["state"] = 'normal'
    button_C["state"] = 'normal'
    button_D["state"] = 'normal'
    button_E["state"] = 'normal'
    button_F["state"] = 'normal'

    button_0["state"] = 'normal'
    button_1["state"] = 'normal'
    button_2["state"] = 'normal'
    button_3["state"] = 'normal'
    button_4["state"] = 'normal'
    button_5["state"] = 'normal'
    button_6["state"] = 'normal'
    button_7["state"] = 'normal'
    button_8["state"] = 'normal'
    button_9["state"] = 'normal'


def set_Oct():
    clear()

    button_A["state"] = 'disabled'
    button_B["state"] = 'disabled'
    button_C["state"] = 'disabled'
    button_D["state"] = 'disabled'
    button_E["state"] = 'disabled'
    button_F["state"] = 'disabled'

    button_0["state"] = 'normal'
    button_1["state"] = 'normal'
    button_2["state"] = 'normal'
    button_3["state"] = 'normal'
    button_4["state"] = 'normal'
    button_5["state"] = 'normal'
    button_6["state"] = 'normal'
    button_7["state"] = 'normal'
    button_8["state"] = 'disabled'
    button_9["state"] = 'disabled'


def set_Bin():
    clear()

    button_A["state"] = 'disabled'
    button_B["state"] = 'disabled'
    button_C["state"] = 'disabled'
    button_D["state"] = 'disabled'
    button_E["state"] = 'disabled'
    button_F["state"] = 'disabled'

    button_0["state"] = 'normal'
    button_1["state"] = 'normal'
    button_2["state"] = 'disabled'
    button_3["state"] = 'disabled'
    button_4["state"] = 'disabled'
    button_5["state"] = 'disabled'
    button_6["state"] = 'disabled'
    button_7["state"] = 'disabled'
    button_8["state"] = 'disabled'
    button_9["state"] = 'disabled'


root = Tk()
root.title("Computer Science Calculator & Converter")

base_set = IntVar()
base_set.set(10)

inputBox = Entry(root)
inputBox.grid(row=0, column=0, columnspan=6, padx=pad_x, pady=pad_y)

history = Label(root, text="History", relief="ridge", borderwidth=border_width)
history.grid(row=0, column=5, rowspan=7)

# <editor-fold desc="Create and place action buttons">
button_equal = Button(root, text="=", padx=pad_x, pady=pad_y)
button_add = Button(root, text="+", padx=pad_x, pady=pad_y)
button_subtract = Button(root, text="-", padx=pad_x, pady=pad_y)
button_multiply = Button(root, text="x", padx=pad_x, pady=pad_y)
button_divide = Button(root, text="/", padx=pad_x, pady=pad_y)

button_clear = Button(root, text="Clear", padx=pad_x, pady=pad_y)
button_clear.bind("<Button-1>", delete_click)  # On button left click, run function
button_clear.bind("<Button-2>", clear_click)  # On button middle click, run function

button_equal.grid(row=7, column=3)
button_add.grid(row=6, column=3)
button_subtract.grid(row=5, column=3)
button_multiply.grid(row=4, column=3)
button_divide.grid(row=3, column=3)
button_clear.grid(row=2, column=3)
# </editor-fold>

# <editor-fold desc="Create and place value buttons">
button_0 = Button(root, text="0", padx=pad_x, pady=pad_y, command=lambda: number_click(0))

button_1 = Button(root, text="1", padx=pad_x, pady=pad_y, command=lambda: number_click(1))
button_2 = Button(root, text="2", padx=pad_x, pady=pad_y, command=lambda: number_click(2))
button_3 = Button(root, text="3", padx=pad_x, pady=pad_y, command=lambda: number_click(3))

button_4 = Button(root, text="4", padx=pad_x, pady=pad_y, command=lambda: number_click(4))
button_5 = Button(root, text="5", padx=pad_x, pady=pad_y, command=lambda: number_click(5))
button_6 = Button(root, text="6", padx=pad_x, pady=pad_y, command=lambda: number_click(6))

button_7 = Button(root, text="7", padx=pad_x, pady=pad_y, command=lambda: number_click(7))
button_8 = Button(root, text="8", padx=pad_x, pady=pad_y, command=lambda: number_click(8))
button_9 = Button(root, text="9", padx=pad_x, pady=pad_y, command=lambda: number_click(9))

button_A = Button(root, text="A", padx=pad_x, pady=pad_y, command=lambda: number_click('A'), state='disabled')
button_B = Button(root, text="B", padx=pad_x, pady=pad_y, command=lambda: number_click('B'), state='disabled')
button_C = Button(root, text="C", padx=pad_x, pady=pad_y, command=lambda: number_click('C'), state='disabled')

button_D = Button(root, text="D", padx=pad_x, pady=pad_y, command=lambda: number_click('D'), state='disabled')
button_E = Button(root, text="E", padx=pad_x, pady=pad_y, command=lambda: number_click('E'), state='disabled')
button_F = Button(root, text="F", padx=pad_x, pady=pad_y, command=lambda: number_click('F'), state='disabled')

button_0.grid(row=7, column=1)

button_1.grid(row=6, column=0)
button_2.grid(row=6, column=1)
button_3.grid(row=6, column=2)

button_4.grid(row=5, column=0)
button_5.grid(row=5, column=1)
button_6.grid(row=5, column=2)

button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)

button_A.grid(row=3, column=0)
button_B.grid(row=3, column=1)
button_C.grid(row=3, column=2)

button_D.grid(row=2, column=0)
button_E.grid(row=2, column=1)
button_F.grid(row=2, column=2)
# </editor-fold>

# <editor-fold desc="Create and place base and value functions">
Radiobutton(root, text="Decimal", variable=base_set, value=10, command=set_Decimal). \
    grid(row=0, column=4, padx=pad_x, pady=pad_y, columnspan=1, rowspan=1)
Radiobutton(root, text="Hex", variable=base_set, value=16, command=set_Hex). \
    grid(row=2, column=4, padx=pad_x, pady=pad_y, columnspan=1, rowspan=1)
Radiobutton(root, text="Oct", variable=base_set, value=8, command=set_Oct). \
    grid(row=4, column=4, padx=pad_x, pady=pad_y, columnspan=1, rowspan=1)
Radiobutton(root, text="Binary", variable=base_set, value=1, command=set_Bin). \
    grid(row=6, column=4, padx=pad_x, pady=pad_y, columnspan=1, rowspan=1)

Decimal_value = Label(root, text="", relief="ridge", borderwidth=border_width, width=values_width). \
    grid(row=1, column=4, padx=pad_x, pady=pad_y, columnspan=1, rowspan=1)
Hex_value = Label(root, text="", relief="ridge", borderwidth=border_width). \
    grid(row=3, column=4, padx=pad_x, pady=pad_y, columnspan=1, rowspan=1)
Oct_value = Label(root, text="", relief="ridge", borderwidth=border_width). \
    grid(row=5, column=4, padx=pad_x, pady=pad_y, columnspan=1, rowspan=1)
Bin_value = Label(root, text="", relief="ridge", borderwidth=border_width). \
    grid(row=7, column=4, padx=pad_x, pady=pad_y, columnspan=1, rowspan=1)
# </editor-fold>



root.mainloop()
