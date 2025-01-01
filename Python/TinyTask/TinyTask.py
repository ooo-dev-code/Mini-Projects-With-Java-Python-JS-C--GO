from tkinter import *
import pyautogui
import time

times = int(input("Interval of time between action = "))
    
class App():
    def __init__(self):
        window = Tk()
        
        window.title("Password Generator")
        window.geometry("720x480")
        window.config(background="#000000")
        
        label = Label(window, text="TinyTask, Press the keys to repeat in the entry.", width=720, fg="white", bg="black", font="700")
        label.pack()
        
        frame = Frame(window, bg="black", width=700, height=460)
        frame.pack(expand=YES)

        self.input_value = Entry(frame)
        self.input_value.pack()
        
        def Tinytask():
            value = self.input_value.get()
            print(value)
            
            while True:
                for i in range(len(value)):
                    time.sleep(times)
                    pyautogui.write(value[i])
                    pyautogui.click()
                
        b_put = Button(frame, text="Start", font="Courrier, 30", command=Tinytask)
        b_put.pack(expand=YES)

        window.mainloop()

if __name__ == '__main__':
  App()
