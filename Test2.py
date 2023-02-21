import tkinter as tk

root = tk.Tk("800x480")
root.title("Mon application")
# Définir un icone :
root.iconbitmap(bitmap="logo.ico")
# Personnaliser la couleur de l'arrière-plan de la fenêtre principale :
root.config(bg = "#87CEEB")
# Définir les dimensions par défaut la fenêtre principale :
root.geometry("500x480")

Textes=[]
for i in range(2):
    Textes.append(tk.Label(root))

Textes[0].config(text="Absolute placement")
Textes[0].config(bg='red')
Textes[0].config(fg='white')

Textes[0].place(x=20, y=10)

# label 2
label2 = tk.Label(root,
    text="Relative placement",
    bg='blue',
    fg='white'
)

label2.place(relx=0.8, rely=0.2, relwidth=0.5, anchor='ne')

quitter=tk.Button(root,text="Quitter",command=root.destroy)
quitter.place(relx=0.5, rely=0.9, anchor='center')

root.mainloop()