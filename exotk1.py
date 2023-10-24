import tkinter as tk

def inscription():
    pseudo = pseudoText.get()
    mdp = mdpText.get()
    email = emailText.get()
    
    if pseudo and mdp and email:
        print("Vous etes bien inscrit")
        print("Voici votre pseudo", pseudo)
        print("Voici votre mot de passe: ", mdp)
        print("Voilà votre email:", email)
        
fenetre = tk.Tk()
fenetre.title("Inscription")

pseudoText = tk.Entry(fenetre, text="Pseudo:")
pseudoText.pack()
pseudoEntry = tk.Entry(fenetre)
pseudoEntry.pack()

mdpText = tk.Entry(fenetre, text="Mot de passe:")
mdpText.pack()
mdpEntry = tk.Entry(fenetre, show="*")
mdpEntry.pack()

emailText = tk.Entry(fenetre, text="E-mail:")
emailText.pack()
emailEntry = tk.Entry(fenetre)
emailEntry.pack()

bouton = tk.Button(fenetre, text="Enregistrez-vous", command=inscription)
bouton.pack()


fenetre.geometry("400x300")
fenetre.mainloop()