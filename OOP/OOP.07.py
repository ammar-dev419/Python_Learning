class Score:
    def __init__(self, player_name):
        self.player_name = player_name
        self.__points = 0

    def ajouter_points(self, valeur):
        if self.__points + valeur <= 20:
            self.__points += valeur
            print(f"{self.player_name} a {self.__points} points.")
        else:
            print(f"{self.player_name} a atteinte limite (20 points)")
    
    def reset(self):
        self.__points = 0
        print(f"{self.player_name} a reinitialite a 0")

    def get_points(self):
        return self.__points
    
score1 = Score("Ammar")

score1.ajouter_points(3)
score1.ajouter_points(17)
score1.ajouter_points(789)
score1.reset()
score1.ajouter_points(4)
print(score1.get_points())