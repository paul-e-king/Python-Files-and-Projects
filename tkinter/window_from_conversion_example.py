from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        feet_entry.delete(0, END) # ignore bad input; just clear the dialog

root = Tk()
root.title("Metric coversion (Feet to Meters)")

mainFrame = ttk.Frame(root, padding="3 3  12 12")
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainFrame, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainFrame, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainFrame, text="Calculate", command=calculate).grid(column=1, row=3, sticky=W)
ttk.Button(mainFrame, text="Quit", command=root.destroy).grid(column=3, row=3, sticky=E)

ttk.Label(mainFrame, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainFrame, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainFrame, text="meters").grid(column=3, row=2, sticky=W)

for child in mainFrame.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
