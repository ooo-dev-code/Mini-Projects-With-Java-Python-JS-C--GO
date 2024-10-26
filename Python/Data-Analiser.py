from tkinter import *
import time
import pandas as pd

class App():
    def __init__(self):
        
        self.file = ""
        self.file_name = ""
        self.data = ""
        
        self.w = Tk()
        self.w.geometry("760x400")
        self.w.configure(bg="black")
        self.w.title("Datas-Analizer")
            
        def DataAnalisis():
            self.file_name = self.file_name_entry.get()
            try:
                self.file = pd.read_csv(f"{self.file_name}")
                print(self.file)
                file_content = Label(self.w, text=f"{self.file}")
                file_content.pack()
                file_columns = Label(self.w, text=f"There is: {self.file.shape[1]} columns")
                file_columns.pack(anchor="e")
            except Exception as e:
                print(f"{e}")
        
        self.file_name_entry = Entry(self.w)
        self.file_name_entry.pack()
        Organize_btn = Button(self.w, text="Organize", command=DataAnalisis)
        Organize_btn.pack(anchor="n")

        self.w.mainloop()
        
if __name__ == "__main__":
    App()

