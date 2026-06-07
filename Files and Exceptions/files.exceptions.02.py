import os
def analyser_notes(nom_fichier):
    dossier = os.path.dirname(__file__)
    chemin = os.path.join(dossier, nom_fichier)
    try:
        with open(chemin, "r") as f:
            lignes = f.read().splitlines()
            if not lignes:
                raise ValueError(" Le fichier est vide.")
            nombres = [int(ligne) for ligne in lignes]
            total = sum(nombres)
            return {
                "meilleure_note": max(nombres),
                "pire_note": min(nombres),
                "somme_notes": total,
                "moyenne": total / len(nombres)
            }
    except FileNotFoundError:
        print(f" Erreur : le fichier '{nom_fichier}' n'existe pas dans le dossier.")
        return None
    except ValueError as ve:
        print(f" Erreur dans le contenu du fichier {ve}")
        return None
    except Exception as e:
        print(f" Une erreur inattandue s'est produite : {e}")
        return None
resultat = analyser_notes("notes_eleves.txt")
if resultat:
    print(f" La meilleure note est : {resultat['meilleure_note']}")
    print(f" La pire note est : {resultat['pire_note']}")
    print(f" La somme des notes est : {resultat['somme_notes']}")
    print(f" La moyenne est : {resultat['moyenne']}")