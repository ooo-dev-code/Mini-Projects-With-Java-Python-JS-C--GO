import tkinter as tk
from tkinter import scrolledtext
import subprocess

def run_code():
    code = code_input.get("1.0", tk.END)
    try:
        output = subprocess.check_output(['python', '-c', code], stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        output = e.output
    output_display.delete("1.0", tk.END)
    output_display.insert(tk.END, output)

# Create the main window
root = tk.Tk()
root.title("Python")

# Create a text area for code input
code_input = scrolledtext.ScrolledText(root, width=80, height=20)
code_input.pack(padx=10, pady=10)

# Create a button to run the code
run_button = tk.Button(root, text="Run Code", command=run_code)
run_button.pack(pady=5)

# Create a text area for output display
output_display = scrolledtext.ScrolledText(root, width=80, height=10)
output_display.pack(padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
