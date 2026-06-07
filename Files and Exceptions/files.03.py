import os 
def analyser_fichier(nom_fichier):
    dossier = os.path.dirname(__file__)
    chemin = os.path.join(dossier, nom_fichier)
    with open(chemin, "r") as f:
        nombres = [int(ligne) for ligne in f.read().splitlines()]
        return {
            "count": len(nombres),
            "sum": sum(nombres),
            "max": max(nombres),
            "min": min(nombres)
        }
resultat = analyser_fichier("values.txt")
if resultat:
    print(f" Le compteur des nombres dans le fichier est : {resultat['count']}")
    print(f" La somme des nombre dans ce fichier est : {resultat['sum']}")
    print(f" Le nombre le plus grand dans ce fichier est : {resultat['max']}")
    print(f" Le nombre le plus petit dans ce fichier est : {resultat['min']}")