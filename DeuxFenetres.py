import tkinter as tk
from tkinter import messagebox


def Action1():
    Fenetre2()


def Action2():
    Fenetre1()


# ---------------------------------------------------------------
def Fenetre1():
    root.title("Fenetre 1")
    # Personnaliser la couleur de l'arrière-plan de la fenêtre principale :
    root.config(bg=couleur_fond1)
    # Définir les dimensions par défaut la fenêtre principale :
    root.geometry("300x200")

    Textes[0].config(text="Nom :")
    Textes[0].config(bg=couleur_fond1)
    Textes[0].place(x=20, y=10)

    Saisies[0].focus()
    Saisies[0].place(x=150, y=10)

    code = tk.Button(root, text="Fenetre 2", command=Action1)
    code.place(x=20, rely=0.7, anchor='w')


def Fenetre2():
    root.title("Fenetre 2")
    # Personnaliser la couleur de l'arrière-plan de la fenêtre principale :
    root.config(bg=couleur_fond2)
    # Définir les dimensions par défaut la fenêtre principale :
    root.geometry("400x300")

    Textes[0].config(text="Prenom")
    Textes[0].config(bg=couleur_fond2)
    Textes[0].place(x=20, y=10)

    Saisies[0].focus()
    Saisies[0].place(x=150, y=10)

    code = tk.Button(root, text="Fenetre 1", command=Action2)
    code.place(x=20, rely=0.7, anchor='w')


# ---------------------------- MAIN -----------------------------
couleur_fond1="#B5EED1"
couleur_fond2="#f4c3b8"

root = tk.Tk()


Textes=[]
for i in range(1):
    Textes.append(tk.Label(root))


Saisies=[]
Variables=[]
for i in range(1):
    v=tk.StringVar()
    Variables.append(v)
    Saisies.append(tk.Entry(root,textvariable=v))


Fenetre1()

quitter=tk.Button(root,text="Quitter",command=root.destroy)
quitter.place(relx=0.5, rely=0.9, anchor='center')

root.mainloop()