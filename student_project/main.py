import file_utils
resultat = file_utils.analyser_scores("scores.txt")
if resultat:
    print(" Resultat:")
    print(f" Le nombre des notes est : {resultat['nombre']}")
    print(f" La meilleure note : {resultat['meilleure']}")
    print(f" La pire note : {resultat['pire']}")
    print(f" Moyenne : {resultat['moy']}")
else:
    print(" Impossible d'analyser les scores")