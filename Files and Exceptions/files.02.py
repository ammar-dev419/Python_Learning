import os
def somme_fichier(nom_fichier):
    dossier = os.path.dirname(__file__)
    chemin = os.path.join(dossier, nom_fichier)
    with open(chemin, "r") as f:
        lignes = f.read().splitlines()
        somme = 0
        for ligne in lignes:
            somme += int(ligne)
        return somme 
resultat = somme_fichier("numbers.txt")
print("La somme des nombres est : ",resultat)