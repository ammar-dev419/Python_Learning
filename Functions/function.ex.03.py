def moyenne_eleve(eleve):
    if not eleve["notes"]:
        return None
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

        if moy is None:
            continue

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
        "echoue" :echoue
    }

eleves = [
    {"nom": "Ali", "notes": [12, 15, 9], "absences" : 2},
    {"nom": "Sara", "notes": [10, 8, 12], "absences" : 5},
    {"nom": "Youssef", "notes": [18, 17, 16], "absences" : 0},
    {"nom": "Ali", "notes": [], "absences" : 1},
]

resultat = statistiques_classe(eleves)
print(f" Meilleur eleve : {resultat['meilleur_eleve']} ({resultat['meilleur_moy']})") 
print(f" Pire eleve : {resultat['pire_eleve']} ({resultat['pire_moy']})") 
print(f" Reussites : {resultat['reussit']}")
print(f" Echecs : {resultat['echoue']}")