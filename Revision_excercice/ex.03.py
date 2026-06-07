text = """Ahmed:14,16,12,18
Sara:19,20,15,17
Ali:10,12,14"""
eleves = []
for ligne in text.split("\n"):
    parties = ligne.split(":")
    notes_str = parties[1].split(",")
    notes = []
    for note in notes_str:
        notes.append(int(note))
    eleve = {
        "nom": parties[0],
        "notes": notes
    }
    eleves.append(eleve)
for eleve in eleves:
        notes = eleve["notes"]
        moyenne = sum(notes) / len(notes)
        eleve["moyenne"] = moyenne
for eleve in eleves:
    print(eleve["nom"],  "-> moyenne:", eleve["moyenne"])