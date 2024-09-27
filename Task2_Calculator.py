import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("320x400")
root.configure(bg="black")


expression = ""


def update_display(value):
    global expression
    expression += value
    display_var.set(expression)


def clear_display():
    global expression
    expression = ""
    display_var.set("0")


def calculate():
    global expression
    try:
        result = str(eval(expression))  
        display_var.set(result)
        expression = result
    except:
        display_var.set("Error")
        expression = ""


display_var = tk.StringVar()
display_var.set("0")
display = tk.Label(root, textvariable=display_var, font=("Arial", 24), bg="black", fg="white", anchor="e", padx=10)
display.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=30, sticky="nsew")


style = ttk.Style()
style.theme_use('alt')  


style.configure("TButton", font=("Arial", 18), foreground="white", background="gray", padding=10)
style.map("TButton", background=[('active', 'darkgray')], foreground=[('active', 'white')])


buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]


for i, row in enumerate(buttons):
    for j, button_text in enumerate(row):
        button = ttk.Button(root, text=button_text, style="TButton",
                            command=lambda x=button_text: update_display(x) if x != "=" else calculate())
        button.grid(row=i + 1, column=j, ipadx=10, ipady=20, sticky="nsew")


clear_button = ttk.Button(root, text="C", style="TButton", command=clear_display)
clear_button.grid(row=5, column=0, columnspan=2, ipadx=88, ipady=20, sticky="nsew")


equal_button = ttk.Button(root, text="=", style="TButton", command=calculate)
equal_button.grid(row=5, column=2, columnspan=2, ipadx=88, ipady=20, sticky="nsew")


root.grid_columnconfigure((0, 1, 2, 3), weight=1)
root.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)


root.mainloop()
