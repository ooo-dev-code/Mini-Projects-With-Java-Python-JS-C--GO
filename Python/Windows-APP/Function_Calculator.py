import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
import math

width = 880
height = 780 

class App():
    def __init__(self):
        
        w = Tk()
        w.title("Calculator")
        w.geometry("400x500")
        w.resizable(False, False)
        
        def draw_function():
            a = int(self.inputs["a"].get())
            b = int(self.inputs["b"].get())
            c = int(self.inputs["c"].get())            
            plt.figure().add_subplot(111, polar=False)
            plt.title("parabole")
            plt.xlabel("x")
            plt.ylabel("y")
            plt.legend(["y = ax^2+bx+c"])
            x = np.linspace(-10, 10, 100)
            y = a*(x**2) + b*x + c
            plt.plot(x, y)
            derivative = f"2*{a}*x+{b}"
            if b**2-4*a*c > 0:
                solution = f"x1 = {(-b+math.sqrt(b**2-4*a*c))/(2*a)}\nx2 = {(-b-math.sqrt(b**2-4*a*c))/(2*a)}"
                sol = Label(frame, text=solution, font = "Helvetica 24 bold")
                sol.grid(row=2, column=0)
                deriv = Label(frame, text=derivative, font = "Helvetica 24 bold")
                deriv.grid(row=3, column=0)
                print(solution)
                print(derivative)
                plt.show()
                plt.close()
            elif b**2-4*a*c == 0:
                solution = f"x = {-b/(2*a)}"
                sol = Label(frame, text=solution, font = "Helvetica 24 bold")
                sol.grid(row=2, column=0)
                deriv = Label(frame, text=derivative, font = "Helvetica 24 bold")
                deriv.grid(row=3, column=0)
                print(solution)
                print(derivative)
                plt.show()
                plt.close()
            else:
                solution = "no solution"
                sol = Label(frame, text=solution, font = "Helvetica 24 bold")
                sol.grid(row=2, column=0)
                deriv = Label(frame, text="derivative = " + derivative, font = "Helvetica 24 bold")
                deriv.grid(row=3, column=0)
                print(solution)
                print(derivative)
                plt.show()
                plt.close()
        
        letters = ["a", "b", "c"]
        self.inputs = {}
        pos_y = [0, 100, 200, 300]
        for i in range(len(letters)):
            frame = Frame(w)
            frame.place(x=0, y=pos_y[i])
            
            self.a = Label(frame, text=letters[i]+"=", font = "Helvetica 34 bold")
            self.a.grid(row=0, column=0)
            
            self.input_a = Entry(frame, font = "Helvetica 34 bold")
            self.inputs[letters[i]] = self.input_a
            self.inputs[letters[i]].grid(row=0, column=1)
            
        btn = Button(w, text="Draw", font = "Helvetica 34 bold", command=draw_function)
        btn.place(x=0, y=400)
        
        w.mainloop()

if __name__ == "__main__":
    app = App()
    
