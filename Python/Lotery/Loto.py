from tkinter import *
from Values import *
import time
import random

class App():
    def __init__(self):
        self.w = Tk()
        
        self.w.title("Loto")
        self.w.configure(bg="black")
        self.w.geometry(f"{width}x{height}")
        
        self.title = Label(self.w, text="Play the loto and win absolutely nothing !!!", background="white")
        self.title.pack()
        
        self.canvas = Canvas(self.w, background="azure2", width=width-25, height=height-100)
        self.canvas.pack(expand=YES)
        
        self.canvas.create_rectangle(canvas_width-25, canvas_height/2+100, canvas_width+(25-canvas_width), canvas_height/2-100, fill="gold")
        
        self.canvas.create_rectangle(canvas_width-25, canvas_height/2+100, canvas_width+(25-canvas_width)*(2/3), canvas_height/2-100, fill="gold")
        self.canvas.create_rectangle(canvas_width-25, canvas_height/2+100, canvas_width+(25-canvas_width)*(1/3), canvas_height/2-100, fill="gold")
            
        def roll():

            for i in range(3):
                
                result[f"value{i+1}"]= random.randint(1, 3)
                print(result[f"value{i+1}"])
        
        def Play():
            
            roll()

            # Drawing in the slots
            if result["value1"] == 1:
                self.canvas.create_rectangle(place1["x1"], place1["y1"], place1["x2"], place1["y2"], fill=color[1])
            elif result["value1"] == 2:
                self.canvas.create_rectangle(place1["x1"], place1["y1"], place1["x2"], place1["y2"], fill=color[2])
            elif result["value1"] == 3:
                self.canvas.create_rectangle(place1["x1"], place1["y1"], place1["x2"], place1["y2"], fill=color[3])
                
            if result["value2"] == 1:
                self.canvas.create_rectangle(place2["x1"], place2["y1"], place2["x2"], place2["y2"], fill=color[1])
            elif result["value2"] == 2:
                self.canvas.create_rectangle(place2["x1"], place2["y1"], place2["x2"], place2["y2"], fill=color[2])
            elif result["value2"] == 3:
                self.canvas.create_rectangle(place2["x1"], place2["y1"], place2["x2"], place2["y2"], fill=color[3])
                
            if result["value3"] == 1:
                self.canvas.create_rectangle(place3["x1"], place3["y1"], place3["x2"], place3["y2"], fill=color[1])
            elif result["value3"] == 2:
                self.canvas.create_rectangle(place3["x1"], place3["y1"], place3["x2"], place3["y2"], fill=color[2])
            elif result["value3"] == 3:
                self.canvas.create_rectangle(place3["x1"], place3["y1"], place3["x2"], place3["y2"], fill=color[3])
                

            # Message when you win
            if result["value1"] == 1 and result["value2"] == 1 and result["value3"] == 1:
                self.win = Label(self.w, text="YOU WON !!!!!!!!!!!!")
                self.win.pack(anchor="n")
            elif result["value1"] == 2 and result["value2"] == 2 and result["value3"] == 2:
                self.win = Label(self.w, text="YOU WON !!!!!!!!!!!!")
                self.win.pack(anchor="n")
            elif result["value1"] == 3 and result["value2"] == 3 and result["value3"] == 3:
                self.win = Label(self.w, text="YOU WON !!!!!!!!!!!!")
                self.win.pack(anchor="n")
        
        self.button = Button(self.w, text="Play", command=Play)
        self.button.pack(anchor="s")
        
        self.w.mainloop()
        
if __name__ == '__main__':
    App()
