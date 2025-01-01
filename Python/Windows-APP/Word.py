import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

val = 15

class WordApp:
    global val
    def __init__(self, root):
        self.root = root
        self.root.title("Word App")
        self.root.geometry("800x600")

        self.text_area = ScrolledText(self.root, wrap=tk.WORD, undo=True, font = ("Times New Roman", val))
        self.text_area.pack(fill=tk.BOTH, expand=1)
        
        self.create_menu()
    
    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        
        size = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Size", menu=size)
        size.add_command(label="10", command=self.size_10)
        size.add_command(label="15", command=self.size_15)
        size.add_command(label="20", command=self.size_20)
        size.add_command(label="25", command=self.size_25)
        size.add_command(label="30", command=self.size_30)
        size.add_command(label="35", command=self.size_35)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=lambda: self.root.focus_get().event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copy", command=lambda: self.root.focus_get().event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", command=lambda: self.root.focus_get().event_generate("<<Paste>>"))
        edit_menu.add_command(label="Select All", command=lambda: self.text_area.tag_add("sel", "1.0", "end"))

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))

    def save_as_file(self):
        self.save_file()
    
    def size_10(self):
        self.text_area.config(font = ("Times New Roman", 10))
    def size_15(self):
        self.text_area.config(font = ("Times New Roman", 15))
    def size_20(self):
        self.text_area.config(font = ("Times New Roman", 20))
    def size_25(self):
        self.text_area.config(font = ("Times New Roman", 25))
    def size_30(self):
        self.text_area.config(font = ("Times New Roman", 30))
    def size_35(self):
        self.text_area.config(font = ("Times New Roman", 35))   

if __name__ == "__main__":
    root = tk.Tk()
    app = WordApp(root)
    root.mainloop()
