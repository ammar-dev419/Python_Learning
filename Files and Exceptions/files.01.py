import os
def somme_notes():
    dossier = os.path.dirname(__file__)
    chemin = os.path.join(dossier,"notes.txt")
    with open(chemin, "r") as f:
        lignes = f.read().splitlines()
        somme = 0
        for ligne in lignes:
            somme += int(ligne)
        return somme
resultat = somme_notes()
print("La somme des notes est : ",resultat)
import os 
print("Play file", os.getcwd())
print("Where is thi file located", __file__)
print("This file folder", os.path.dirname(__file__))