import tkinter as tk
from tkinter import ttk, messagebox


contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if not name or not phone:
        messagebox.showerror("Input Error", "Name and Phone Number are required.")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    update_contact_list()
    update_dropdown()
    clear_entries()

def update_contact_list():
    for row in contact_tree.get_children():
        contact_tree.delete(row)
    for contact in contacts:
        contact_tree.insert("", "end", values=(contact["name"], contact["phone"]))

def search_contact():
    search_term = search_entry.get().lower()
    filtered_contacts = [c for c in contacts if search_term in c["name"].lower() or search_term in c["phone"].lower()]
    contact_tree.delete(*contact_tree.get_children())
    for contact in filtered_contacts:
        contact_tree.insert("", "end", values=(contact["name"], contact["phone"]))

def on_select(event):
    selected_item = contact_tree.selection()
    if not selected_item:
        return
    index = contact_tree.index(selected_item)
    contact = contacts[index]
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    name_entry.insert(0, contact["name"])
    phone_entry.insert(0, contact["phone"])
    email_entry.insert(0, contact["email"])
    address_entry.insert(0, contact["address"])

def update_contact():
    selected_item = contact_tree.selection()
    if not selected_item:
        messagebox.showerror("Selection Error", "No contact selected.")
        return
    index = contact_tree.index(selected_item)
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if not name or not phone:
        messagebox.showerror("Input Error", "Name and Phone Number are required.")
        return
    
    contacts[index] = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    update_contact_list()
    update_dropdown()
    clear_entries()

def delete_contact():
    selected_item = contact_tree.selection()
    if not selected_item:
        messagebox.showerror("Selection Error", "No contact selected.")
        return
    index = contact_tree.index(selected_item)
    contacts.pop(index)
    update_contact_list()
    update_dropdown()
    clear_entries()

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def update_dropdown():
    contact_names = [contact["name"] for contact in contacts]
    contact_dropdown['values'] = contact_names

def view_contact_from_dropdown(event):
    selected_name = contact_dropdown.get()
    for contact in contacts:
        if contact["name"] == selected_name:
            name_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            address_entry.delete(0, tk.END)
            name_entry.insert(0, contact["name"])
            phone_entry.insert(0, contact["phone"])
            email_entry.insert(0, contact["email"])
            address_entry.insert(0, contact["address"])
            break


root = tk.Tk()
root.title("Contact Book")
root.geometry("800x600")
root.configure(bg="#2E2E2E")


tk.Label(root, text="Name:", background="#2E2E2E", foreground="white").grid(row=0, column=0, padx=10, pady=5, sticky='w')
name_entry = tk.Entry(root, width=50, justify='center')
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone Number:", background="#2E2E2E", foreground="white").grid(row=1, column=0, padx=10, pady=5, sticky='w')
phone_entry = tk.Entry(root, width=50, justify='center')
phone_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email:", background="#2E2E2E", foreground="white").grid(row=2, column=0, padx=10, pady=5, sticky='w')
email_entry = tk.Entry(root, width=50, justify='center')
email_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Address:", background="#2E2E2E", foreground="white").grid(row=3, column=0, padx=10, pady=5, sticky='w')
address_entry = tk.Entry(root, width=50, justify='center')
address_entry.grid(row=3, column=1, padx=10, pady=5)

button_frame = tk.Frame(root, bg="#2E2E2E")
button_frame.grid(row=4, column=0, columnspan=2, pady=10)

tk.Button(button_frame, text="Add Contact", command=add_contact).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Update Contact", command=update_contact).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Delete Contact", command=delete_contact).pack(side=tk.LEFT, padx=5)

tk.Label(root, text="Search:", background="#2E2E2E", foreground="white").grid(row=5, column=0, padx=10, pady=5, sticky='w')
search_entry = tk.Entry(root, width=50, justify='center')
search_entry.grid(row=5, column=1, padx=10, pady=5, sticky='w')
tk.Button(root, text="Search Contact", command=search_contact).grid(row=5, column=2, padx=10, pady=5, sticky='w')

tk.Label(root, text="View Contact:", background="#2E2E2E", foreground="white").grid(row=6, column=0, padx=10, pady=5, sticky='w')
contact_dropdown = ttk.Combobox(root, width=50)
contact_dropdown.grid(row=6, column=1, padx=10, pady=5)
contact_dropdown.bind("<<ComboboxSelected>>", view_contact_from_dropdown)


contact_tree = ttk.Treeview(root, columns=("Name", "Phone"), show="headings", height=15)
contact_tree.heading("Name", text="Name")
contact_tree.heading("Phone", text="Phone Number")
contact_tree.grid(row=7, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

contact_tree.bind("<ButtonRelease-1>", on_select)


root.grid_rowconfigure(7, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=0)


update_dropdown()


root.mainloop()
