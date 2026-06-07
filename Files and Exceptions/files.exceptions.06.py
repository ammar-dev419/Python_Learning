import os 
def sum_moy_notes(nom_fichier):
    dossier = os.path.dirname(__file__)
    chemin = os.path.join(dossier, nom_fichier)
    try:
        with open(chemin, "r") as f:
            lignes = f.read().splitlines()
            if not lignes:
                raise ValueError(" Le fichier est vide.")
            notes = [int(ligne) for ligne in lignes]
            return {
                "sum_notes": sum(notes),
                "moy_notes": sum(notes) / len(notes)
            }
    except FileNotFoundError:
        print(f" Le fichier '{nom_fichier}' n'existe pas dans le dossier.")
        return None
    except ValueError as ve:
        print(f" Erreur dans le contenu du fichier : '{ve}'")
        return None
    except Exception as e:
        print(f" Une erreur inattandue produite : {e}")
        return None
def afficher_resultat(nom_fichier, resultat):
    dossier = os.path.dirname(__file__)
    chemin = os.path.join(dossier, nom_fichier)
    try:
        with open(chemin, "a") as f:
            f.write("\n")
            f.write("----Resume----\n")
            f.write(f" La somme de notes est : {resultat['sum_notes']}\n")
            f.write(f" La moyenne est : {resultat['moy_notes']:.2f}\n")
    except Exception as e:
        print(f" Une erreur inattandue produite : {e}")
        return None
resultat = sum_moy_notes("scores.txt")
if resultat:
    afficher_resultat("scores.txt", resultat)
    print(" Le programme a ete creer avec succes")