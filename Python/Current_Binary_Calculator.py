from tkinter import *

width = 720
height = 660
line_nums = 10
a=0

class App():
    def __init__(self):
        
        w = Tk()
        w.geometry(f"{width}x{height}")
        w.title("Binary")
        
        table = Canvas(w, width=width, height=height/2+60, bg="grey")
        table.pack()
        
        for i in range(line_nums):
            a = table.create_line((width/line_nums)*i+35, 35, (width/line_nums)*i+35, height/2+30, fill="black", width=20)
            
        def hello(event):
            print("Single Click, Button-l") 
        
        table.bind('<Button-1>', hello)
        w.mainloop()
        
if __name__ == "__main__":
    App()
