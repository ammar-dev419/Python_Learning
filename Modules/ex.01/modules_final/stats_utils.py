def somme(liste):
    return sum(liste)

def moyenne(liste):
    return sum(liste) / len(liste)

liste = [14, 5, 76, 9, 32]

if __name__ == "__main__":
    print("Somme",somme(liste) )
    print("Moyenne", moyenne(liste))