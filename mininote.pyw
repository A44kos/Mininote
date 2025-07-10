import os, tkinter as tk
from tkinter import filedialog as fd

class Mininote:
    def __init__(self, root):
        root.title("Untitled - Minipad")
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.ico")
        root.iconbitmap(icon_path)

        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Create New ", command=self.new_file)
        self.file_menu.add_command(label="Open File  ", command=self.open_file)
        self.file_menu.add_command(label="Save File  ", command=self.save_file)

        self.text_editor = tk.Text(root, undo="1")
        self.text_editor.pack(expand=True, fill="both")
        self.file_path = None

    def new_file(self):
        root.title("Untitled - Minipad")
        self.text_editor.delete(1.0, tk.END)
        self.file_path = None

    def open_file(self):
        file_path = fd.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("Python files", "*.py"), ("PyW files", "*.pyw"), ("Batch files", "*.bat"), ("Configuration files", "*.ini"), ("Javascript files", "*.js"), ("VBScript files", "*.vbs"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file: content = file.read()
            self.text_editor.delete(1.0, tk.END)
            self.text_editor.insert(tk.END, content)
            self.update_title(file_path)

    def save_file(self):
        file_path = fd.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("Python files", "*.py"), ("PyW files", "*.pyw"), ("Batch files", "*.bat"), ("Configuration files", "*.ini"), ("Javascript files", "*.js"), ("VBScript files", "*.vbs"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                content = self.text_editor.get(1.0, tk.END)
                file.write(content)
            self.update_title(file_path)
            self.file_path = file_path

    def update_title(self, file_path):
        root.title(os.path.basename(file_path) + " - Minipad")

if __name__ == "__main__":
    root = tk.Tk()
    app = Mininote(root)
    root.mainloop()