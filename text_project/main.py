import text_utils
resultat = text_utils.analyser_texte("text.txt")
if resultat:
    print(f" Le nombre des lignes dans le texte est : {resultat['nb_lignes']}")
    print(f" Le nombre des mots dans le texte est : {resultat['nb_mots']}")
    print(f" Le nombre des lettres dans le texte est : {resultat['nb_lettre']}")
    print(f" Le mot le plus grand est : {resultat['max_mot']}")
    print(f" Le mot le plus petit est : {resultat['min_mot']}")
else:
    print(" Impossible d'analyser le texte.")
print(" Fin du programme")