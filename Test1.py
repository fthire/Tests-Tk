import tkinter as tk

root = tk.Tk("800x480")
root.title("Mon application")
# Définir un icone :
root.iconbitmap("logo.ico")
# Personnaliser la couleur de l'arrière-plan de la fenêtre principale :
root.config(bg = "#87CEEB")
# Définir les dimensions par défaut la fenêtre principale :
root.geometry("500x480")

label1 = tk.Label(
    root,
    text="Absolute placement",
    bg='red',
    fg='white'
)

label1.place(x=20, y=10)

# label 2
label2 = tk.Label(
    root,
    text="Relative placement",
    bg='blue',
    fg='white'
)

label2.place(relx=0.8, rely=0.2, relwidth=0.5, anchor='ne')
root.mainloop()