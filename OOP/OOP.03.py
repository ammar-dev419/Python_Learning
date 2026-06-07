class Voiture:
    def __init__(self, marque, couleur):
        self.marque = marque
        self.couleur = couleur
        self.__vitesse = 0

    def accelerer(self, valeur):
        if valeur > 0:
            self.__vitesse += valeur
        print(f"La {self.marque} accelerer a {self.__vitesse} km/h")

    def freiner(self, valeur):
        if valeur > 0:
            self.__vitesse = max(0, self.__vitesse -valeur)
        print(f"La {self.marque} ralentit a {self.__vitesse} km/h")

    def changer_couleur(self, nouvelle_couleur):
        self.couleur = nouvelle_couleur
        print(f"La couleur de {self.marque} est maintenant {self.couleur}")

class Conducteur:
    def __init__(self, nom, voiture):
        self.nom = nom
        self.voiture = voiture

    def conduire(self):
        print(f"{self.nom} conduit la {self.voiture.marque} de couleur {self.voiture.couleur}")

voiture1 = Voiture("BMW", "Noir")
voiture2 = Voiture("Audi", "Blanc")

conducteur1 = Conducteur("Ali", voiture1)
conducteur2 = Conducteur("Sare", voiture2)

conducteur1.conduire()
conducteur2.conduire()

voiture1.accelerer(60)
voiture1.freiner(30)

voiture2.accelerer(50)
voiture2.freiner(60)

voiture1.changer_couleur("Rouge")
conducteur1.conduire()