from tkinter import *
from tkinter import ttk

def check_winner():

    for i in range(1, 4):
        if buttons[(i, 1)]["text"] == buttons[(i, 2)]["text"] == buttons[(i, 3)]["text"] != " ":
            return buttons[(i, 1)]["text"]

    for i in range(1, 4):
        if buttons[(1, i)]["text"] == buttons[(2, i)]["text"] == buttons[(3, i)]["text"] != " ":
            return buttons[(1, i)]["text"]

    if buttons[(1, 1)]["text"] == buttons[(2, 2)]["text"] == buttons[(3, 3)]["text"] != " ":
        return buttons[(1, 1)]["text"]
    if buttons[(1, 3)]["text"] == buttons[(2, 2)]["text"] == buttons[(3, 1)]["text"] != " ":
        return buttons[(1, 3)]["text"]

    if all(buttons[pos]["text"] != " " for pos in buttons):
        return "Empate"

    return None

def on_button_click(pos):
    global turn
    button = buttons[pos]
    if button["text"] == " ":
        button["text"] = "X" if turn % 2 == 1 else "O"
        turn += 1
        winner = check_winner()
        if winner:
            if winner == "Empate":
                mensaje.set("¡Es un empate!")
            else:
                mensaje.set(f"¡Ganó {winner}!")
        elif turn > 9:
            mensaje.set("¡Es un empate!")
        else:
            mensaje.set(f"Turno de {'X' if turn % 2 == 1 else 'O'}")

def restart_game():
    global turn
    turn = 1
    mensaje.set("Turno de X")
    for button in buttons.values():
        button["text"] = " "

root = Tk()
root.geometry('300x200')
root.title("Juego de Tic-Tac-Toe") 

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mensaje = StringVar()
mensaje.set("Turno de X")
ttk.Label(mainframe, textvariable=mensaje).grid(column=1, row=4, sticky=(W, E))

buttons = {}
turn = 1

positions = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
for lugarb in positions:
    button = ttk.Button(mainframe, text=" ", width=5, command=lambda p=lugarb: on_button_click(p))
    button.grid(column=lugarb[0], row=lugarb[1], sticky=W)
    buttons[lugarb] = button

restart_btn = ttk.Button(mainframe, text="Reiniciar", command=restart_game)
restart_btn.grid(column=1, row=5, sticky=(W, E))

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()