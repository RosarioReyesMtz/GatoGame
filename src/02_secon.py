from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        mensaje.set("Mensaje")
    except ValueError:
        pass

root = Tk()
root.geometry('300x150')
root.title("Mensaje en una etiqueta") 

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mensaje = StringVar()
ttk.Label(mainframe, textvariable=mensaje).grid(column=1, row=4, sticky=(W, E))

ttk.Button(mainframe, text="[ ]", command=calculate).grid(column=1, row=1, sticky=W)
ttk.Button(mainframe, text="[ ]", command=calculate).grid(column=1, row=2, sticky=W)
ttk.Button(mainframe, text="[ ]", command=calculate).grid(column=1, row=3, sticky=W)
ttk.Button(mainframe, text="[ ]", command=calculate).grid(column=2, row=1, sticky=W)
ttk.Button(mainframe, text="[ ]", command=calculate).grid(column=2, row=2, sticky=W)
ttk.Button(mainframe, text="[ ]", command=calculate).grid(column=2, row=3, sticky=W)
ttk.Button(mainframe, text="[ ]", command=calculate).grid(column=3, row=1, sticky=W)
ttk.Button(mainframe, text="[ ]", command=calculate).grid(column=3, row=2, sticky=W)
ttk.Button(mainframe, text="[ ]", command=calculate).grid(column=3, row=3, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.bind("<Return>", calculate)

root.mainloop()