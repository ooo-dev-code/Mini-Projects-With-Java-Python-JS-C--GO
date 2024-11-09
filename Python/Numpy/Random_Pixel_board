from tkinter import *
import numpy as np

face = np.random.randint(0, 255, [300, 300])
print(face)
print(face[0][1])

width = 300
height = 300

x = 1
y = 1

w = Tk()
w.geometry(f'{width}x{height}')
w.title('Square')

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb   


canvas = Canvas(w, width=width, height=height, bg='grey')
canvas.pack()

for i in range(width//2):
    for j in range(height//2):
        canvas.create_rectangle(i*x*2, j*y*2, i*x*2+1, j*y*2+1, outline=_from_rgb((face[i][j], face[i][j], face[i][j])), fill='red')

w.mainloop()
