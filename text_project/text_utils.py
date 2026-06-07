import os
def analyser_texte(nom_fichier):
    dossier = os.path.dirname(__file__)
    chemin = os.path.join(dossier, nom_fichier)
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            lignes = f.read().splitlines()
            if not lignes:
                raise ValueError(" Le fichier est vide.")
            mots = []
            nb_lettre = 0
            for ligne in lignes:
                mots_ligne = ligne.split()
                mots.extend(mots_ligne)
                for mot in mots_ligne:
                    nb_lettre += len(mot)
            if not mots:
                raise ValueError(" Le fichier ne comtient aucun mot.")
            return {
                "nb_lignes": len(lignes),
                "nb_mots": len(mots),
                "nb_lettre": nb_lettre,
                "max_mot": max(mots, key=len),
                "min_mot": min(mots, key=len)
            }
    except FileNotFoundError:
        print(" Le fichier n'existe pas dans le dossier.")
    except ValueError as ve:
        print(f" Erreur dans le contanue du fichier : '{ve}'")
    except Exception as e:
        print(f" Une erreur inattandue produite : '{e}'")
    return None