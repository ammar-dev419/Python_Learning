class Voiture:
    def __init__(self, marque, couleur, vitesse):
        self.marque = marque
        self.couleur = couleur
        self.vitesse = vitesse

    def afficher_info(self):
        print(f"Marque: {self.marque} => Couleur: {self.couleur} => Vitesse: {self.vitesse}")
        
voiture1 = Voiture("Audi", "rouge", "220 km/h")
voiture2 = Voiture("Bugatti", "bleue", "240 km/h")
voiture1.afficher_info()
voiture2.afficher_info()