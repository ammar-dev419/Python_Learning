import os

def lire_et_analyser_fichier(nom_fichier):

    """
    Cette fonction lit in fichier contenant les notes des etudiants, 
    et retourne une liste de dictionnaires, un dictionnaires par etudiant.
    """

    dossier = os.path.dirname(__file__)
    chemin = os.path.join(dossier, nom_fichier)
    liste_eleves = []

    try:
        with open(chemin, "r", encoding="utf-8") as f:
            lignes = f.read().splitlines()

        if not lignes:
            raise ValueError(" Le fichier est vide.")
        
        for ligne in lignes:
            if ":" not in ligne:
                print(f" Ligne ignoree (pas de ':') : {ligne}")
                continue
            nom_part, notes_part = ligne.split(":", 1)
            nom = nom_part.strip()
            if not nom:
                print(f" Ligne ignoree (nom vide) : {ligne}")
                continue
            try:
                notes = [int(note) for note in notes_part.strip().split()]
            except ValueError:
                print(f" Ligne ignoree (note invalide) : {ligne}")
                continue
            eleve = {
                "nom": nom,
                "notes": notes
            }
            liste_eleves.append(eleve)
        if not liste_eleves:
            raise ValueError(" Aucun etudiant valide trouve dans le fichier.")
        return liste_eleves
    except FileNotFoundError:
        print(" Le fichier n'existe pas.")
    except ValueError as ve:
        print(f" Erreur : {ve}")
    except Exception as e:
        print(f" Erreur inattendue : {e}")
    return None

def calculer_statistiques(liste_eleves):
    """
    Cette fonctions calcule les statistiques pour chaque etudiant et 
    trouve l'etudiant avec la meilleure moyenne.
    """
    if not liste_eleves:
        return None
    for eleve in liste_eleves:
        notes = eleve["notes"]
        eleve["moyenne"] = round(sum(notes)/len(notes), 2)
        eleve["max"] = max(notes)
        eleve["min"] = min(notes)
    meilleur_eleve = max(liste_eleves, key=lambda e :e["moyenne"])
    stats = {
        "nombre_eleves": len(liste_eleves),
        "meilleur_eleve": meilleur_eleve,
        "liste_eleves": liste_eleves
    }
    return stats