eleve = {
    "nom": "Ahmed",
    "notes": [14, 16, 12, 18]
}
moy = sum(eleve["notes"]) / len(eleve["notes"])
eleve["moyenne"] = moy
print(eleve)