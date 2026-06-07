import os 
def analyser_mots(nom_fichier):
    dossier = os.path.dirname(__file__)
    chemin = os.path.join(dossier, nom_fichier)
    try:
        with open(chemin, "r") as f:
            mots = f.read().splitlines()
            if not mots:
                raise ValueError(" Le fichier est vide.")
            nombre_mots = len(mots)
            mot_plus_long = max(mots, key=len)
            mot_plus_court = min(mots, key=len)
            return {
                "nombre_mots": nombre_mots,
                "longueur_max": len(mot_plus_long),
                "longueur_min": len(mot_plus_court)
            }
    except FileNotFoundError:
        print(f" Le fichier '{nom_fichier}' n'existe pas dans le dossier.")
        return None
    except ValueError as ve:
        print(f" Erreur dans le contenu du fichier '{ve}'")
        return None
    except Exception as e:
        print(f" Une erreur inattandue produite : '{e}'")
        return None
def afficher_resultats(nom_fichier, resultat):
    dossier = os.path.dirname(__file__)
    chemin = os.path.join(dossier, nom_fichier)
    try:
        with open(chemin, "w") as f:
            f.write(f" Le nombre de mots est : {resultat['nombre_mots']}\n")
            f.write(f" Longueur du mot le plus long est : {resultat['longueur_max']}\n")
            f.write(f" Longueur du mot le plus court est : {resultat['longueur_min']}")
    except Exception as e:
        print(f" Une erreur inattandue produite : '{e}'")
        return None
resultat = analyser_mots("mots.txt")
if resultat:
    afficher_resultats("rapport_mots.txt", resultat)
    print(" Le rapport a ete creer avec succes.")