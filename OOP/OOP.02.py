class Voiture:
    def __init__(self, marque, couleur):
        self.marque = marque
        self.couleur = couleur
        self.vitesse = 0

    def accelerer(self, valeur):
        self.vitesse += valeur
        print(f"La {self.marque} accelerer a {self.vitesse} km/h")

    def freiner(self, valeur):
        self.vitesse = max(0, self.vitesse - valeur)
        print(f"La {self.marque} ralentit a {self.vitesse} km/h")

class Conducteur:
    def __init__(self, nom, voiture):
        self.nom = nom
        self.voiture = voiture

    def conduire(self):
        print(f"{self.nom} conduit la {self.voiture.marque}")
        
ma_voiture = Voiture("BMW", "Noir" )
conducteur1 = Conducteur("Ali", ma_voiture)
conducteur1.conduire()
ma_voiture.accelerer(50)
ma_voiture.freiner(20)