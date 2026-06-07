import os
def analyser_temperatures(nom_fichier):
    dossier = os.path.dirname(__file__)
    chemin = os.path.join(dossier, nom_fichier)
    try:
        with open(chemin, "r") as f:
            lignes = f.read().splitlines()
            if not lignes:
                raise ValueError(" Le fichier est vide.")
            temperature = [int(ligne) for ligne in lignes]
            return {
                "max_temp": max(temperature),
                "min_temp": min(temperature),
                "moy_temp": sum(temperature) / len(temperature)
        }
    except FileNotFoundError:
        print(f" Erreur : le fichier '{nom_fichier}' n'existe pas dans le dossier")
        return None
    except ValueError as ve:
        print(f" Erreur dans le contenu du fichier : {ve}")
        return None
    except Exception as e:
        print(f" Une erreur inattandue produite : {e}")
        return None
def rapport_temperatures(nom_fichier, resultat):
    dossier = os.path.dirname(__file__)
    chemin = os.path.join(dossier, nom_fichier)
    try:
        with open(chemin, "w") as f:
            f.write(f" La temperature la plus elevee est :{resultat['max_temp']}\n")
            f.write(f" La temperature la plus basse est : {resultat['min_temp']}\n")
            f.write(f" La moyenne du temperature est : {resultat['moy_temp']:.2f}\n")
    except Exception as e:
        print(f" Erreur lors du l'ecriture du fichier : {e}")
resultat = analyser_temperatures("temperatures.txt")
if resultat:
    rapport_temperatures("rapport_temperature.txt", resultat)
    print(" Le rapport a ete creer avec succes")