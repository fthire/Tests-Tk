import tkinter as tk


def Action1():
    Textes[2].config(text=Variables[0].get())

# ---------------------------- MAIN -----------------------------
root = tk.Tk("800x480")
root.title("Machine Enigma")
# Définir un icone :
root.iconbitmap("logo.bmp")
# Personnaliser la couleur de l'arrière-plan de la fenêtre principale :
root.config(bg = "#87CEEB")
# Définir les dimensions par défaut la fenêtre principale :
root.geometry("500x480")

Textes=[]
for i in range(3):
    Textes.append(tk.Label(root))

Saisies=[]
Variables=[]
for i in range(1):
    v=tk.StringVar()
    Variables.append(v)
    Saisies.append(tk.Entry(root,textvariable=v))

Textes[0].config(text="Message à coder : ")
Textes[0].config(bg='#87CEEB')
Textes[0].place(x=20, y=10)

Textes[1].config(text="Message codé : ")
Textes[1].config(bg='#87CEEB')
Textes[1].place(x=20, y=50)

Textes[2].config(text="")
Textes[2].config(bg='#87CEEB')
Textes[2].place(x=150, y=50)


Saisies[0].focus()
Saisies[0].place(x=150, y = 10)

code=tk.Button(root,text="Code",command=Action1)
code.place(relx=0.5, rely=0.8, anchor='center')

quitter=tk.Button(root,text="Quitter",command=root.destroy)
quitter.place(relx=0.5, rely=0.9, anchor='center')

root.mainloop()