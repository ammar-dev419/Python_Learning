from student_utils import lire_et_analyser_fichier, calculer_statistiques
liste_eleves = lire_et_analyser_fichier("students.txt")
if liste_eleves:
    stats = calculer_statistiques(liste_eleves)
    print(f" Nombre d'etudiants : {stats['nombre_eleves']}")
    print(f" Meilleur eleve : {stats['meilleur_eleve']['nom']} (moyenne = {stats['meilleur_eleve']['moyenne']})\n")
    print(" Details :")
    for e in stats["liste_eleves"]:
        print(f"- {e['nom']} sa moyenne est : {e['moyenne']}, max : {e['max']}, min : {e['min']}")