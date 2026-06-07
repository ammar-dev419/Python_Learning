def moyenne_eleve(eleve):
    return sum(eleve["notes"]) / len(eleve["notes"]) 

def statistiques_classe(eleves):
    meilleur_moy = -1
    pire_moy = float("inf")
    meilleur_eleve = ""
    pire_eleve = ""
    reussit = 0
    echoue = 0
    for eleve in eleves:
        moy = moyenne_eleve(eleve)
        if moy > meilleur_moy:
            meilleur_moy = moy 
            meilleur_eleve = eleve["nom"]
        if moy < pire_moy:
            pire_moy = moy 
            pire_eleve = eleve["nom"]
        if moy >= 10 and eleve["absences"] < 5:
            reussit += 1
        else:
            echoue += 1
    return {
        "meilleur_eleve": meilleur_eleve,
        "meilleur_moy": meilleur_moy,
        "pire_eleve": pire_eleve,
        "pire_moy": pire_moy,
        "reussit": reussit,
        "echoue": echoue
    }
def eleves_absents(eleves):
    return [eleve["nom"] for eleve in eleves if eleve["absences"] >= 5]

def activite_populaire(eleves):
    compteur = {}
    for eleve in eleves:
        for activite in eleve["activites"]:
            compteur[activite] = compteur.get(activite, 0) + 1
    return max(compteur, key=compteur.get)

def resume_classe(eleves):
    stats = statistiques_classe(eleves)
    absents = eleves_absents(eleves)
    activite = activite_populaire(eleves)
    return stats, absents, activite

eleves = [
    {"nom": "Ali", "notes": [12, 15, 9], "absences": 2,"activites": ["foot", "piano"]},
    {"nom": "Sara", "notes": [10, 8, 12], "absences": 5,"activites": ["piano"]},
    {"nom": "Youssef", "notes": [18, 17, 16], "absences": 0,"activites": ["foot", "chess"]},
    {"nom": "Lina", "notes": [7, 6, 8], "absences": 8,"activites": ["chess"]}
]

stats, absents, activite = resume_classe(eleves)

print(" Statistiques de la classe : ")
print(f" Meilleur eleve : {stats['meilleur_eleve']} ({stats['meilleur_moy']:.2f})")
print(f" Pire eleve : {stats['pire_eleve']} ({stats['pire_moy']:.2f})")
print(f" Reussites : {stats['reussit']}")
print(f" Echecs : {stats['echoue']}\n")
print(f" Eleves absents (>= 5) : {absents}")
print(f" Activite la plus populaire : {activite}")