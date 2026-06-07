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
                "meilleur_note": max(nombres),
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
def sauvegarder_resultats(nom_fichier, resultat):
    dossier = os.path.dirname(__file__)
    chemin = os.path.join(dossier, nom_fichier)
    try:
        with open(chemin, "w") as f:
            f.write(f" Meilleure note : {resultat['meilleur_note']}\n")
            f.write(f" Pire note : {resultat['pire_note']}\n")
            f.write(f" Somme des notes : {resultat['somme_notes']}\n")
            f.write(f" Moyenne : {resultat['moyenne']:.2f}\n")
    except Exception as e:
        print(f" Erreur lors de l'ecriture du fichier : {e}")
resultat = analyser_notes("notes_eleves.txt")
if resultat:
    sauvegarder_resultats("rapport.txt", resultat)
    print("Le rapport a ete cree avec succes.")