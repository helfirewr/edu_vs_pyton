import tkinter as tk

window = tk.Tk()

def spinValue():
    label.config(text = str(spin.get()) )

spin = tk.Spinbox(window, from_ = 0, to = 50, command=spinValue)
spin.pack()

label = tk.Label(window)
label.pack()

window.mainloop()