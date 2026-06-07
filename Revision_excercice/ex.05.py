import os
dossier = os.path.dirname(__file__)
chemin = os.path.join(dossier, "numbers.txt")
try:
    with open(chemin, "r", encoding="utf-8") as f:
        lignes = f.read().splitlines()
        if not lignes:
            raise ValueError(" Le fichier est vide.")
        for ligne in lignes:
            nombres = [float(ligne) for ligne in lignes]
            somme = sum(nombres)
            moy = somme / len(nombres)
        print(f"somme: {somme}")
        print(f"Moyenne: {moy:.2f}")
except FileNotFoundError:
    print(" Le fichier n'existe pas dans le dossier.")
    print(None)
except ValueError as ve:
    print(f" Erreur dans le contenue du fichier: {ve}")
    print(None)
except Exception as e:
    print(f" Une erreur inattandue produite: {e}")
    print(None)