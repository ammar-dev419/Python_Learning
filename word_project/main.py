import text_utils
resultat = text_utils.analyser_texte("texte.txt")
if resultat:
    print(" Resultat:")
    print("-" * 20)
    print(f" Le nombre des lignes dans le texte est : {resultat['nb_lignes']}")
    print(f" Le nombre des mots dans le texte est : {resultat['nb_mots']}")
    print(f" Nombre de fois ou chaque mot est repete est : {resultat['compteur_mots']}")
    print(f" Le le plus repete est : {resultat['max_mots']}")
    print(f" Le le moins repete est : {resultat['min_mots']}")
else:
    print(" Impossible d'analyser le teste.")
print(" Fin du programme")