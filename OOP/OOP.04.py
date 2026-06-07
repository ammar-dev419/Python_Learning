class Voiture:
    def __init__(self, marque, couleur):
        self.marque = marque
        self.couleur = couleur
        self.__vitesse = 0

    def afficher_info(self):
        print(f"Marque: {self.marque}")
        print(f"couleur: {self.couleur}")
        print(f"Vitesse: {self.__vitesse} km/h")
        print("-" * 30)

    def accelerer(self, valeur):
        if valeur > 0:
            self.__vitesse += valeur
        print(f"La {self.marque} accelerer a {self.__vitesse} km/h")

    def freiner(self, valeur):
        if valeur > 0:
            self.__vitesse = max(0, self.__vitesse - valeur)
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

    def accelerer_voiture(self, valeur):
        print(f"{self.nom} accelerer la voiture")
        self.voiture.accelerer(valeur)

    def freiner_voiture(self, valeur):
        print(f"{self.nom} freine la voiture")
        self.voiture.freiner(valeur)

voiture1 = Voiture("Toyota", "Bleu")
conducteur1 =Conducteur("Ali", voiture1)

conducteur1.conduire()

conducteur1.accelerer_voiture(40)
conducteur1.accelerer_voiture(20)
conducteur1.freiner_voiture(30)
conducteur1.freiner_voiture(50)

voiture1.afficher_info()

voiture1.changer_couleur("Rouge")
conducteur1.conduire()