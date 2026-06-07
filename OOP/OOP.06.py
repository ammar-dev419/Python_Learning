class Compteurlimit:
    def __init__(self, nom):
        self.nom = nom
        self.__valeur = 0

    def incrementer(self):
        if self.__valeur < 5:
            self.__valeur += 1
            print(f"{self.nom} = {self.__valeur}")
        else:
            print(f"{self.nom} a atteinte limite(5)")

    def reset(self):
        self.__valeur = 0
        print(f"{self.nom} a ete reinitialise a 0")

    def get_valeur(self):
        return self.__valeur
    
compte = Compteurlimit("Mon compteur")
for _ in range(7):
    compte.incrementer()
compte.reset()
compte.incrementer()
print(compte.get_valeur())
