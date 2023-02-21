import tkinter as tk
from tkinter import messagebox


def Action1():
    ident=Variables[0].get()
    mdp=Variables[1].get()
    mdp2=Variables[2].get()
    if mdp != mdp2:
        print("Mots de passe différents !")
        tk.messagebox.showwarning("Attention","Mots de passe différents !")
    else:
        code.place_forget()
    print(ident,mdp,mdp2)

# ---------------------------- MAIN -----------------------------
couleur_fond="#B5EED1"
root = tk.Tk("800x480")
root.title("Création compte")
# Personnaliser la couleur de l'arrière-plan de la fenêtre principale :
root.config(bg = couleur_fond)
# Définir les dimensions par défaut la fenêtre principale :
root.geometry("300x200")

Textes=[]
for i in range(3):
    Textes.append(tk.Label(root))

Textes[0].config(text="Identifiant      : ")
Textes[0].config(bg=couleur_fond)
Textes[0].place(x=20, y=10)

Textes[1].config(text="Mot de passe     : ")
Textes[1].config(bg=couleur_fond)
Textes[1].place(x=20, y=50)

Textes[2].config(text="Confirmation mdp : ")
Textes[2].config(bg=couleur_fond)
Textes[2].place(x=20, y=90)

Saisies=[]
Variables=[]
for i in range(3):
    v=tk.StringVar()
    Variables.append(v)
    Saisies.append(tk.Entry(root,textvariable=v))


Saisies[0].focus()
Saisies[0].place(x=150, y = 10)
Saisies[1].place(x=150, y = 50)
Saisies[2].place(x=150, y = 90)

code=tk.Button(root,text="Inscription",command=Action1)
code.place(x=20, rely=0.7, anchor='w')

quitter=tk.Button(root,text="Quitter",command=root.destroy)
quitter.place(relx=0.5, rely=0.9, anchor='center')

root.mainloop()