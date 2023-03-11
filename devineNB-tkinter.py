import tkinter as tk
import random

def Valider():
	nb_propose=int(nb.get())
	if nb_propose==nb_trouver:
		message="Gagné !"
	elif nb_propose > nb_trouver:
		message="Plus petit !"
	else:
		message = "Plus grand !"
	Wtexte.config(text=message)
	Wid.delete(0,tk.END)


# ------------------------------------------------------------------------------------------------------
nb_trouver=random.randint(1,100)

fen1 = tk.Tk()
fen1.title("Jeu Devine Nombre")
couleur='PaleTurquoise1'
fen1.configure(background=couleur)

# Les questions
tk.Label(fen1, text="Votre nombre ", bg=couleur,fg="black").grid(row=0,column=0)

# Les réponses
nb=tk.StringVar()
Wid=tk.Entry(textvariable=nb, width=30)
Wid.grid(row=0,column=1)

# Affichage de la réponse
Wtexte= tk.Label(fen1, text="",bg=couleur,fg="dodgerblue4",font=('Times New Roman', 15, 'bold'))
Wtexte.grid(row=1,columnspan=2)

# un bouton pour valider
tk.Button(fen1,text="Valider",bg="royal blue",fg="SteelBlue1",command=Valider).grid(row=2,columnspan=2)
tk.Button(fen1,text="Quitter",bg="firebrick",fg="snow",command=fen1.quit).grid(row=3,columnspan=2)
fen1.mainloop()
