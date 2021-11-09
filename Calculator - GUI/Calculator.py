from tkinter import *

global stored_num, fnum, math_action

flag1 = False

pad_x = 15
pad_y = 10
border_width = 3
values_width = 20
entry_width = 20
history_width = 35
history_height = 20

root = Tk()
root.title("Computer Science Calculator & Converter")


def clear_history():
    history_val.delete(1.0,END)


def update_history(num1, act, num2, result):
    text = str(num1) + act + str(num2) + '=' + str(result) + '\n'
    history_val.insert(1.0, text)


def equal_click():
    cycle_actions()
    do_math()

    update_conversions()

    global flag1
    flag1 = True


def cycle_conversions():
    if hex_value["state"] == 'disabled':
        hex_value["state"] = 'normal'
        oct_value["state"] = 'normal'
        bin_value["state"] = 'normal'
    else:
        hex_value["state"] = 'disabled'
        oct_value["state"] = 'disabled'
        bin_value["state"] = 'disabled'


def clear_conversions():
    if hex_value["state"] == 'disabled':
        cycle_conversions()

    hex_value.delete(0, len(hex_value.get()))
    oct_value.delete(0, len(oct_value.get()))
    bin_value.delete(0, len(bin_value.get()))

    cycle_conversions()


def update_conversions():

    clear_conversions()

    if hex_value["state"] == 'disabled':
        cycle_conversions()

    cur_value = int(round(float(inputBox.get())))

    # text = "Decimal Value is - " + str(cur_value)
    # decv.set(text)
    text = str(hex(cur_value))
    hex_value.insert(0, text)
    hex_value.delete(0, 2)
    text = str(oct(cur_value))
    oct_value.insert(0, text)
    oct_value.delete(0, 2)
    text = str(bin(cur_value))
    bin_value.insert(0, text)
    bin_value.delete(0, 2)

    cycle_conversions()


def do_math():
    finum = float(fnum)
    snum = float(inputBox.get())
    clear_input()
    res = 0

    if math_action == '+':
        res = finum + snum
        inputBox.insert(0, res)
    elif math_action == '-':
        res = finum - snum
        inputBox.insert(0, res)
    elif math_action == '*':
        res = finum * snum
        inputBox.insert(0, res)
    elif math_action == '/':
        res = finum / snum
        inputBox.insert(0, res)

    update_history(finum, math_action, snum, res)


def store_click():
    number = float(inputBox.get())
    global stored_num
    stored_num = number


def recall_click():
    clear_input()
    inputBox.insert(0, stored_num)
    update_conversions()


# <editor-fold desc="Math button functions">
def action_click():
    global fnum
    fnum = inputBox.get()
    clear_input()
    cycle_actions()


def add_click():
    global math_action
    math_action = '+'
    action_click()


def subtract_click():
    global math_action
    math_action = '-'
    action_click()


def divide_click():
    global math_action
    math_action = '/'
    action_click()


def multiply_click():
    global math_action
    math_action = '*'
    action_click()


# </editor-fold>


def cycle_actions():
    if button_add["state"] == "normal":
        button_add["state"] = "disabled"
        button_subtract["state"] = "disabled"
        button_multiply["state"] = "disabled"
        button_divide["state"] = "disabled"
    else:
        button_add["state"] = "normal"
        button_subtract["state"] = "normal"
        button_multiply["state"] = "normal"
        button_divide["state"] = "normal"


def number_click(entry):
    global flag1
    if flag1:
        clear_input()
        flag1 = False
    length = len(inputBox.get())
    inputBox.insert(length, entry)
    update_conversions()


def clear_click(event):
    clear_input()


def clear_input():
    inputBox.delete(0, END)
    clear_conversions()


def delete_click(event):
    inputBox.delete(len(inputBox.get()) - 1, END)
    update_conversions()


# <editor-fold desc="Change Input Base">
def set_hex():
    clear_input()

    set_decimal()

    button_A["state"] = 'normal'
    button_B["state"] = 'normal'
    button_C["state"] = 'normal'
    button_D["state"] = 'normal'
    button_E["state"] = 'normal'
    button_F["state"] = 'normal'


def set_decimal():
    clear_input()

    set_oct()

    button_8["state"] = 'normal'
    button_9["state"] = 'normal'


def set_oct():
    clear_input()

    set_bin()

    button_2["state"] = 'normal'
    button_3["state"] = 'normal'
    button_4["state"] = 'normal'
    button_5["state"] = 'normal'
    button_6["state"] = 'normal'
    button_7["state"] = 'normal'


def set_bin():
    clear_input()

    button_A["state"] = 'disabled'
    button_B["state"] = 'disabled'
    button_C["state"] = 'disabled'
    button_D["state"] = 'disabled'
    button_E["state"] = 'disabled'
    button_F["state"] = 'disabled'

    button_2["state"] = 'disabled'
    button_3["state"] = 'disabled'
    button_4["state"] = 'disabled'
    button_5["state"] = 'disabled'
    button_6["state"] = 'disabled'
    button_7["state"] = 'disabled'
    button_8["state"] = 'disabled'
    button_9["state"] = 'disabled'


base_set = IntVar()
base_set.set(10)
# </editor-fold>

inputBox = Entry(root)
inputBox.grid(row=0, column=0, columnspan=3, padx=pad_x, pady=pad_y)

ms_button = Button(root, text="Store Value", padx=pad_x, pady=pad_y, command=store_click)

history_lbl = Label(root, text="History", relief="ridge", borderwidth=border_width)
history_lbl.grid(row=0, column=5, rowspan=1, columnspan=1)

history_button = Button(root, text="Clear History", padx=pad_x, pady=pad_y, command=clear_history)
history_button.grid(row=0, column=6, rowspan=1, columnspan=1)

history_val = Text(root, height=history_height, width=history_width)
history_val.grid(row=1, column=5, rowspan=6, columnspan=2, padx=pad_x, pady=pad_y)

# <editor-fold desc="Create and place action buttons">
button_equal = Button(root, text="=", padx=pad_x, pady=pad_y, command=equal_click)
button_add = Button(root, text="+", padx=pad_x, pady=pad_y, command=add_click)
button_subtract = Button(root, text="-", padx=pad_x, pady=pad_y, command=subtract_click)
button_multiply = Button(root, text="x", padx=pad_x, pady=pad_y, command=multiply_click)
button_divide = Button(root, text="/", padx=pad_x, pady=pad_y, command=divide_click)

button_clear = Button(root, text="Clear", padx=pad_x, pady=pad_y)
button_clear.bind("<Button-1>", delete_click)  # On button left click, run function
button_clear.bind("<Button-2>", clear_click)  # On button middle click, run function

button_equal.grid(row=7, column=3)
button_add.grid(row=6, column=3)
button_subtract.grid(row=5, column=3)
button_multiply.grid(row=4, column=3)
button_divide.grid(row=3, column=3)
button_clear.grid(row=2, column=3)

button_ms = Button(root, text="MS", padx=pad_x, pady=pad_y, command=store_click)
button_mr = Button(root, text="MR", padx=pad_x, pady=pad_y, command=recall_click)

button_ms.grid(row=0, column=3)
button_mr.grid(row=1, column=3)
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

# <editor-fold desc="Create and place base and value displays">

'''
Decimal_value = Label(root, text='Decimal -', relief="ridge", borderwidth=border_width, width=values_width). \
    grid(row=1, column=4, padx=pad_x, pady=pad_y, columnspan=1, rowspan=1)
'''

hex_lbl = Label(root, text='Hexadecimal value -', relief="ridge", borderwidth=border_width). \
    grid(row=2, column=4, padx=pad_x, pady=pad_y, columnspan=1, rowspan=1)
oct_lbl = Label(root, text='Octal value - ', relief="ridge", borderwidth=border_width). \
    grid(row=4, column=4, padx=pad_x, pady=pad_y, columnspan=1, rowspan=1)
bin_lbl = Label(root, text='Binary value - ', relief="ridge", borderwidth=border_width). \
    grid(row=6, column=4, padx=pad_x, pady=pad_y, columnspan=1, rowspan=1)

hex_value = Entry(root, state='disabled')
hex_value.grid(row=3, column=4, padx=pad_x, pady=pad_y, columnspan=1, rowspan=1)
oct_value = Entry(root, state='disabled')
oct_value.grid(row=5, column=4, padx=pad_x, pady=pad_y, columnspan=1, rowspan=1)
bin_value = Entry(root, state='disabled')
bin_value.grid(row=7, column=4, padx=pad_x, pady=pad_y, columnspan=1, rowspan=1)

# </editor-fold>


root.mainloop()
