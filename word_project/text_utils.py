import os
def analyser_texte(nom_fichier):
    dossier = os.path.dirname(__file__)
    chemin = os.path.join(dossier, nom_fichier)
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            lignes = f.read().splitlines()
            if not lignes:
                raise ValueError(" Le fichier est vide.")
            compteur = {}
            for ligne in lignes:
                for mot in ligne.lower().split():
                    compteur[mot] = compteur.get(mot, 0) + 1
            if not compteur:
                    raise ValueError(" Le fichier ne contient aucun mot.")
            return {
                "nb_lignes": len(lignes),
                "nb_mots": sum(compteur.values()),
                "compteur_mots": compteur,
                "max_mots": max(compteur, key=compteur.get),
                "min_mots": min(compteur, key=compteur.get)
            }
    except FileNotFoundError:
        print(f" Le fichier '{nom_fichier}' n'existe pas dans le dossier.")
    except ValueError as ve:
        print(f" Erreur dans le continue du fichier : '{ve}'")
    except Exception as e:
        print(f" Une erreur inattandue produite : '{e}'")
    return None