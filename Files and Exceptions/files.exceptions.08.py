import os
def lire_notes(nom_fichier):
    dossier = os.path.dirname(__file__)
    chemin = os.path.join(dossier, nom_fichier)
    notes = []
    try:
        with open(chemin, "r") as f:
            for ligne in f:
                ligne = ligne.strip()
                if not ligne:
                    continue
                try:
                    note = float(ligne)
                    notes.append(note)
                except ValueError:
                    print(f" Valeur invalide ignoree : {ligne}")
        if not notes:
            raise ValueError(" Le fichier ne contient aucune note valide.")
        return notes
    except FileNotFoundError:
        print(" Le fichier n'existe pas dans le dossier.")
        return None
    except Exception as e:
        print(f" Une erreur inattandue produite : '{e}'")
        return None
def analyser_notes(notes):
    print("\n Analyser les notes.")
    print("-" * 20)
    print(f" Nombres des notes est : {len(notes)}")
    print(f" La meilleure note est : {max(notes)}")
    print(f" La pire note est : {min(notes)}")
    print(f" La moyenne est : {sum(notes) / len(notes):.2f}")
resultat = lire_notes("grades.txt")
if resultat:
    analyser_notes(resultat)
else:
    print("\n Les notes ne peuvent pas etre analysees")
print(" Fin du programme")