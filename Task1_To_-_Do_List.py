import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font

class ResizableSidebarTodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

       
        self.root.geometry("600x400")
        self.root.config(bg="#282828")


        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)


        self.sidebar = tk.Frame(self.root, bg="#1a1a1a", padx=10, pady=10)
        self.sidebar.grid(row=0, column=0, sticky="ns")
        self.sidebar.grid_rowconfigure(0, weight=1)  


        self.main_frame = tk.Frame(self.root, bg="#282828", padx=20, pady=20)
        self.main_frame.grid(row=0, column=1, sticky="nsew")


        self.title_label = tk.Label(self.sidebar, text="Tasks", font=("Arial", 16, "bold"), fg="white", bg="#1a1a1a")
        self.title_label.pack(pady=10)


        self.task_listbox = tk.Listbox(self.sidebar, font=("Arial", 12), bg="#333333", fg="white", 
                                       selectbackground="#444444", height=15, borderwidth=0, relief="flat")
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


        self.scrollbar = ttk.Scrollbar(self.sidebar, orient="vertical", command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)


        self.task_entry = tk.Entry(self.main_frame, font=("Arial", 14), bg="#333333", fg="white", relief="flat")
        self.task_entry.pack(fill=tk.X, pady=(0, 10))
        self.task_entry.insert(0, "Enter a task...")


        self.task_entry.bind("<FocusIn>", self.clear_placeholder)
        self.task_entry.bind("<FocusOut>", self.restore_placeholder)
        self.task_entry.bind("<Return>", lambda event: self.add_task())


        self.buttons_frame = tk.Frame(self.main_frame, bg="#282828")
        self.buttons_frame.pack(fill=tk.X)


        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 12), padding=6)

        self.add_button = ttk.Button(self.buttons_frame, text="Add Task", command=self.add_task, style="TButton")
        self.add_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        self.update_button = ttk.Button(self.buttons_frame, text="Update Task", command=self.update_task, style="TButton")
        self.update_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        self.delete_button = ttk.Button(self.buttons_frame, text="Delete Task", command=self.delete_task, style="TButton")
        self.delete_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

    def clear_placeholder(self, event):
        if self.task_entry.get() == "Enter a task...":
            self.task_entry.delete(0, tk.END)

    def restore_placeholder(self, event):
        if not self.task_entry.get():
            self.task_entry.insert(0, "Enter a task...")

    def add_task(self):
        task = self.task_entry.get()
        if task and task != "Enter a task...":
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def update_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            new_task = self.task_entry.get()
            if new_task and new_task != "Enter a task...":
                # Replace the selected task with the new task
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, new_task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a valid task.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ResizableSidebarTodoApp(root)
    root.mainloop()
