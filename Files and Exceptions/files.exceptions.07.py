import os
def lire_fichier(nom_fichier):
    dossier = os.path.dirname(__file__)
    chemin = os.path.join(dossier, nom_fichier)
    try:
        with open("ex.txt", "r") as f:
            contenu = f.read().splitlines()
    except FileNotFoundError:
        print(f" Le fichier '{"ex.txt"}' n'existe pas dans le dossier.")
        return None
    except Exception as e:
        print(" Une erreur inattandue produite ''.")
    else:
        print(" Lecture terminee avec succes.")
        print(contenu)
    finally:
        print(" La tentative a echoue\n")
lire_fichier("ex.txt")