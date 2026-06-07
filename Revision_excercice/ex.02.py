eleves = [
    {"nom": "Ahmed", "notes": [14, 16, 12, 18]},
    {"nom": "Youssef" ,"notes": [7, 20, 13, 16]},
    {"nom": "Sara" ,"notes": [1,15, 17, 19]}
]
for eleve in eleves:
    moy = sum(eleve["notes"]) / len(eleve["notes"])
    eleve["moyenne"] = moy
    print("Nom :", eleve["nom"])
    print("Notes :", eleve['notes'])
    print("Moyenne :", eleve["moyenne"])