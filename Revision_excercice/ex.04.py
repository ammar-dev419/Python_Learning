import os
dossier = os.path.dirname(__file__)
chemin = os.path.join(dossier, "student.txt")
eleves = []
with open(chemin, "r", encoding="utf-8") as f:
    lignes = f.read().splitlines()
for ligne in lignes:
    parties = ligne.split(":")
    nom = parties[0]
    notes_str = parties[1].split()
    notes = []
    for n in notes_str:
        notes.append(int(n))
        eleve = {
            "nom": nom,
            "notes": notes
        }
    eleves.append(eleve)
for eleve in eleves:
    notes = eleve["notes"]
    eleve["moyenne"] = sum(notes) / len(notes)
for eleve in eleves:
    print(f"{eleve["nom"]} -> moyenne:{eleve["moyenne"]:.2f}")