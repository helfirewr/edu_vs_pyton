import tkinter as tk

window = tk.Tk()

scrollbar = tk.Scrollbar(window)
textBox = tk.Text(window, height=5, width=30, padx=5, pady=5,
            font="Times 18 bold" )

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
textBox.pack(side=tk.LEFT, fill=tk.Y)
scrollbar.config(command=textBox.yview)
textBox.config(yscrollcommand = scrollbar.set)

textBox.insert(tk.END, "Hello World! \n Hello Again!")

print("Text data:", textBox.get(1.0, "end") )


window.mainloop()