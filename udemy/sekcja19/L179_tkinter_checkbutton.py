import tkinter as tk

window = tk.Tk()

def valueChanged():
    if cbValue.get() == 0:
        print("CheckButton is off")
    if cbValue.get() == 1:
        print("CheckButton is on")

cbValue = tk.IntVar(value=0)
c1 = tk.Checkbutton(window, text="Accept TOS", variable=cbValue,
        onvalue=1, offvalue=0, command=valueChanged)
c1.grid(row=0)

window.mainloop()