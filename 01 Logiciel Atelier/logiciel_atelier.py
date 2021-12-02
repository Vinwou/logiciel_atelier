
# L'importation de l’ensemble des éléments du paquet tkinter :
from tkinter import *


# Création d'une fenêtre avec la classe Tk :
fenetre = Tk()

# Réglage de la couleur de fond
fenetre.config(background='#FF5733')

# Pour regler la taille de la fenêtre
fenetre.geometry("400x300")




# Pour régler la "petite" taille de la fenêtre
fenetre.minsize(400, 300)


# Définir un icone :
fenetre.iconbitmap("bul1.ico")


# Ajout d'un titre à la fenêtre principale :
fenetre.title("Nom/thème de la fenêtre")



# L'instance Label permet d'afficher du texte
Message1 = Label(fenetre, text='Gestion de commandes atelier', font=('courrier', 15), bg='#FF5733')
Message1.pack()





# Affichage de la fenêtre créée :
fenetre.mainloop()
