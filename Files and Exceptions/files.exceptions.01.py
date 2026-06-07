import os 
def analyser_fichier(nom_fichier):
    dossier = os.path.dirname(__file__)
    chemin = os.path.join(dossier, nom_fichier)
    try:
        with open(chemin, "r") as f:
            lignes = f.read().splitlines()
            if not lignes:
                raise ValueError(" Le fichier est vide.")
            nombres = [int(ligne) for ligne in lignes]
        return {
            "count": len(nombres),
            "sum": sum(nombres),
            "max": max(nombres),
            "min": min(nombres)
        }
    except FileNotFoundError:
        print(f" Erreur : le fichier '{nom_fichier}' n'existe pas dans le dossier.")
        return None
    except ValueError as ve:
        print(f" Erreur dans le contenu du fichier : {ve}")
        return None
resultat = analyser_fichier("values.txt")
if resultat:
    print(f" Le compteur des nombres dans le fichier est : {resultat['count']}")
    print(f" La somme des nombre dans ce fichier est : {resultat['sum']}")
    print(f" Le nombre le plus grand dans ce fichier est : {resultat['max']}")
    print(f" Le nombre le plus petit dans ce fichier est : {resultat['min']}")