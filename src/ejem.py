from tkinter import *
from tkinter import ttk

def calculate(pos):
    mensaje.set(f"Posicion:  {pos}")

root = Tk()
root.geometry('300x150')
root.title("Mensaje en una etiqueta") 

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mensaje = StringVar()
ttk.Label(mainframe, textvariable=mensaje).grid(column=1, row=4, sticky=(W, E))


positions = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
for pos in positions:
    button = ttk.Button(mainframe, text="[ ]", command=lambda p=pos: calculate(p))
    button.grid(column=pos[0], row=pos[1], sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.bind("<Return>", lambda event: calculate((0, 0))) 

root.mainloop()