#python calculator

# WINDOW
import tkinter as tk
from logging import exception
from tkinter import Button

root = tk.Tk()
root.title("MY CALCULATOR WITH UI")
root.geometry("400x500")
root.resizable(False, False)

def button_clicked(value):
    current = entry.get()
    if current == "Error":
        entry.delete(0, tk.END)
    entry.insert(tk.END, value)

def clear_button_clicked():
    entry.delete(0, tk.END)
def backspace():
    current = entry.get()
    if current == "Error":
        entry.delete(0, tk.END)
    else:
        new_text = current[:-1]
        entry.delete(0, tk.END)
        entry.insert(0, new_text)

def calculate_button_clicked(char):
    current = entry.get()
    if current =="Error":
        entry.delete(0, tk.END)
        entry.insert(0, current+str(char))

    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except (SyntaxError, ZeroDivisionError, ValueError):

        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def equal():
    try:

        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def percentage():
    try:
        current = float(entry.get())
        result = current / 100
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# DISPLAY
entry = tk.Entry(
         root,
          font= ("Arial", 24, "bold"),
                 bg="pink",
                 fg="purple",
                 borderwidth=5,
                 relief="raised",
                 justify= "right"
)
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

#ROW-1
btn_ac = tk.Button(root, text="AC", width=10, height=3, command=clear_button_clicked)
btn_percentage = tk.Button(root,text="%", width=10,height=3, command=percentage)
btn_clear = tk.Button(root, text="clear", width=10, height=3, command=backspace)
btn_equal = tk.Button(root, text="=", width=10, height=3, command=equal)
btn_div = tk.Button(root, text="/", width=10, height=3, command=lambda: button_clicked("/"))

btn_ac.grid(row=1, column=0)
btn_percentage.grid(row=1, column=1)
btn_clear.grid(row=1, column=2)
btn_div.grid(row=1, column=3)

#ROW-2
btn_7 = tk.Button(root, text="7", width=10, height=3, command=lambda: button_clicked("7"))
btn_8 = tk.Button(root, text="8", width=10, height=3, command=lambda: button_clicked("8"))
btn_9 = tk.Button(root, text="9", width=10, height=3, command=lambda: button_clicked("9"))
btn_mul = tk.Button(root, text="*", width=10, height=3, command=lambda: button_clicked("*"))

btn_7.grid(row=2, column=0)
btn_8.grid(row=2, column=1)
btn_9.grid(row=2, column=2)
btn_mul.grid(row=2, column=3)

#ROW-3
btn_4 = tk.Button(root, text="4", width=10, height=3, command=lambda: button_clicked("4"))
btn_5 = tk.Button(root, text="5", width=10, height=3, command=lambda: button_clicked("5"))
btn_6 = tk.Button(root, text="6", width=10, height=3, command=lambda: button_clicked("6"))
btn_minus = tk.Button(root, text="-", width=10, height=3, command=lambda: button_clicked("-"))

btn_4.grid(row=3, column=0)
btn_5.grid(row=3, column=1)
btn_6.grid(row=3, column=2)
btn_minus.grid(row=3, column=3)

#ROW-4
btn_1 = tk.Button(root, text="1", width=10, height=3, command=lambda: button_clicked("1"))
btn_2 = tk.Button(root, text="2", width=10, height=3, command=lambda: button_clicked("2"))
btn_3 = tk.Button(root, text="3", width=10, height=3, command=lambda: button_clicked("3"))
btn_plus = tk.Button(root, text="+", width=10, height=3, command=lambda: button_clicked("+"))

btn_1.grid(row=4, column=0)
btn_2.grid(row=4, column=1)
btn_3.grid(row=4, column=2)
btn_plus.grid(row=4, column=3)

#ROW-5
btn_00 = tk.Button(root, text="00", width=10, height=3, command=lambda: button_clicked("00"))
btn_0 = tk.Button(root, text="0", width=10, height=3, command=lambda:button_clicked("0"))
btn_decimal = tk.Button(root, text=".", width=10, height=3, command=lambda: button_clicked("."))
btn_equal = tk.Button(root, text="=", width=10, height=3, command= equal)

btn_equal= tk.Button(
    root,
    text="=",
    width=10,
    height=3,
    bg="pink",
    fg="black",
    activebackground="#ff99ad",
    borderwidth="5",
    relief="raised",
    justify="right",
    command= equal)



btn_00.grid(row=5, column=0)
btn_0.grid(row=5, column=1)
btn_decimal.grid(row=5, column=2)
btn_equal.grid(row=5, column=3)

btn_style={
    "bg" : "pink",
    "fg" : "purple",
    "activebackground" : "#ff99ad",
    "borderwidth" : "5",
    "relief" : "raised",
    "justify" : "right",
}
  #RUN APP
root.mainloop()