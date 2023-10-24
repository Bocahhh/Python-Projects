import tkinter as tk

def action_bouton():
    print("Le bouton a été cliqué")

fenetre = tk.Tk()
fenetre.title("Ma premier interface graphique")

bouton = tk.Button(fenetre, text="Cliquez sur moi", command=action_bouton)
bouton.pack()

champ_texte = tk.Entry(fenetre)
champ_texte.pack

fenetre.geometry("400x300")

fenetre.mainloop()