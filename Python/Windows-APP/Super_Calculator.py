from tkinter import *
import math


width = 480
height = 780 

class App():
    def __init__(self):
        w = Tk()
        w.title("Calculator")
        w.geometry(f"{width}x{height}")
        
        self.value1 = 0
        self.value2 = 0
        self.operation = ""
        self.pow = False
        self.input = Entry(w, font = "Helvetica 34 bold", textvariable=self.value1)
        self.input.place(x=0, y=0, width=width, height=80)
        
        frame = Frame(w)
        frame.place(x=0, y=100)
        
        def set_text(text):
            if self.operation == "=" or self.operation == "pow" or self.operation == "%" or self.operation == "!" or self.operation == "sqrt":
                self.input.delete(0, END)
                self.operation = ""
            self.input.insert(END, str(text))
            return
                
        nums = []
        nums.append(Button(frame, width=int(width/300+3), height=int(height/600), text="0", font = "Helvetica 34 bold", command=lambda: set_text("0")))
        nums.append(Button(frame, width=int(width/300+3), height=int(height/600), text="1", font = "Helvetica 34 bold", command=lambda: set_text("1")))
        nums.append(Button(frame, width=int(width/300+3), height=int(height/600), text="2", font = "Helvetica 34 bold", command=lambda: set_text("2")))
        nums.append(Button(frame, width=int(width/300+3), height=int(height/600), text="3", font = "Helvetica 34 bold", command=lambda: set_text("3")))
        nums.append(Button(frame, width=int(width/300+3), height=int(height/600), text="4", font = "Helvetica 34 bold", command=lambda: set_text("4")))
        nums.append(Button(frame, width=int(width/300+3), height=int(height/600), text="5", font = "Helvetica 34 bold", command=lambda: set_text("5")))
        nums.append(Button(frame, width=int(width/300+3), height=int(height/600), text="6", font = "Helvetica 34 bold", command=lambda: set_text("6")))
        nums.append(Button(frame, width=int(width/300+3), height=int(height/600), text="7", font = "Helvetica 34 bold", command=lambda: set_text("7")))
        nums.append(Button(frame, width=int(width/300+3), height=int(height/600), text="8", font = "Helvetica 34 bold", command=lambda: set_text("8")))
        nums.append(Button(frame, width=int(width/300+3), height=int(height/600), text="9", font = "Helvetica 34 bold", command=lambda: set_text("9")))
        
        def operators(sym):
            if sym == "del":
                self.input.delete(0, END)
            if sym == "!":
                self.value1 = self.input.get()
                self.input.delete(0, END)
                char = []
                self.value1 = int(self.value1)
                for i in range(0, int(self.value1)+1):
                    if not int(self.value1)-i==0:
                        char.append(int(self.value1)-i)
                for i in char:
                    if not i == 1:
                        self.value1 = self.value1*(i-1)
                    print(self.value1, i)
                self.input.insert(0, "=" + str((int(self.value1))))
                self.operation = "!"
                
            if sym == "sqrt":
                self.value1 = self.input.get()
                self.input.delete(0, END)
                self.input.insert(0, "=" + str(math.sqrt(int(self.value1))))
                self.operation = "sqrt"
                
            if sym == "%":
                self.value1 = self.input.get()
                self.value1 = int(self.value1)
                self.value1 /= 100
                self.input.delete(0, END)
                self.input.insert(0, "=" + str((float(self.value1))) + "%")
                self.operation = "%"
                
            if sym == "pow":
                self.value1 = self.input.get()
                self.input.delete(0, END)
                self.operation = "pow"
                self.pow = True
                print(self.value1, self.value2, self.operation)
                
            if sym == "=":
                self.value2 = self.input.get()
                self.input.delete(0, END)
                print(self.value1, self.value2, self.operation)
                
                if self.pow:
                    print(self.value1, self.value2)
                    self.input.insert(0, "=" + str(int(self.value1) ** int(self.value2)))
                    self.pow = False
                self.operation = "="
                
            
        symbols = []
        symbols.append(
            Button(frame, width=int(width/300+3), height=int(height/600), text="%", font = "Helvetica 34 bold", command=lambda: operators("%"))
        )
        symbols.append(
            Button(frame, width=int(width/300+3), height=int(height/600), text="!", font = "Helvetica 34 bold", command=lambda: operators("!"))
        )
        symbols.append(
            Button(frame, width=int(width/300+3), height=int(height/600), text="sqrt", font = "Helvetica 34 bold", command=lambda: operators("sqrt"))
        )
        symbols.append(
            Button(frame, width=int(width/300+3), height=int(height/600), text="pow", font = "Helvetica 34 bold", command=lambda: operators("pow"))
        )
        symbols.append(
            Button(frame, width=int(width/300+3), height=int(height/600), text="=", font = "Helvetica 34 bold", command=lambda: operators("="))
        )
        symbols.append(
            Button(frame, width=int(width/300+3), height=int(height/600), text="del", font = "Helvetica 34 bold", command=lambda: operators("del"))
        )
            
        for i in range(6):
            symbols[i].grid(row=i,column=3,ipady=14) 

        nums[0].grid(row=3,column=1,ipady=14) 
        nums[1].grid(row=0,column=0,ipady=14) 
        nums[2].grid(row=0,column=1,ipady=14) 
        nums[3].grid(row=0,column=2,ipady=14) 
        nums[4].grid(row=1,column=2,ipady=14) 
        nums[5].grid(row=1,column=0,ipady=14) 
        nums[6].grid(row=1,column=1,ipady=14) 
        nums[7].grid(row=2,column=2,ipady=14) 
        nums[8].grid(row=2,column=0,ipady=14) 
        nums[9].grid(row=2,column=1,ipady=14)
                
        
        w.mainloop()

if __name__ == "__main__":
    App()
