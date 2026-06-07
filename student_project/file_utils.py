import os
def analyser_scores(nom_fichier):
    dossier = os.path.dirname(__file__)
    chemin = os.path.join(dossier, nom_fichier)
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            lignes = f.read().splitlines()
        if not lignes:
            raise ValueError(" Le fichier est vide.")
        scores = [float(ligne) for ligne in lignes]
        return {
                "nombre": len(scores),
                "meilleure": max(scores),
                "pire": min(scores),
                "moy": sum(scores) / len(scores)
            }
    except FileNotFoundError:
        print(" Le fichier n'exsite pas dans le dossier.")
    except ValueError as ve:
        print(f" Erreur dans le contenue du fichier : {ve}")
    except Exception as e:
        print(f" Une erreur inattandue produite : {e}")
    return None