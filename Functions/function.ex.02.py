def analyser_pairs_impairs(liste):

    pairs_count = 0
    pairs_sum = 0
    impairs_count = 0
    impairs_sum = 0

    for nombre in liste:
        if nombre % 2 == 0:
            pairs_count += 1
            pairs_sum += nombre
        else:
            impairs_count += 1
            impairs_sum += nombre
    pairs_moyenne = pairs_sum / pairs_count if pairs_count > 0 else 0
    impairs_moyenne = impairs_sum / impairs_count if impairs_count > 0 else 0

    return {
        "pairs": {
            "count": pairs_count,
            "sum": pairs_sum,
            "moyenne": pairs_moyenne
        },
        "impairs": {
            "count": impairs_count,
            "sum": impairs_sum,
            "moyenne": impairs_moyenne
        }
    }

liste = [34, 54, 12, 0, 7, 23]
resultat = analyser_pairs_impairs(liste)
print("Pairs :",resultat["pairs"])
print("Impairs :",resultat["impairs"])