import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    all_chars = lower_case + upper_case + digits + special_chars
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def on_generate():
    try:
        length = int(length_entry.get())
        if length < 1:
            messagebox.showerror("Input Error", "Length must be at least 1.")
            return
        password = generate_password(length)
        result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.configure(bg="#333333")


tk.Label(root, text="Enter the desired length of the password:", bg="#333333", fg="white").pack(pady=10)

length_entry = tk.Entry(root, font=("Arial", 14), justify='center')
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", font=("Arial", 14), command=on_generate)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="Generated Password: ", font=("Arial", 12), bg="#333333", fg="white")
result_label.pack(pady=10)


root.mainloop()
