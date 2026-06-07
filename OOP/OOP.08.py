class LifePoints:
    def __init__(self, player_name):
        self.player_name = player_name
        self.__life = 10

    def take_damage(self, amount):
        if self.__life == 0:
            return f"{self.player_name} est deja mort."
        elif self.__life - amount > 0:
            self.__life -= amount
            return f"Le joueur {self.player_name} a perdu {amount} points du vie."
        else:
            self.__life = 0
            return f"Le joueur {self.player_name} est mort."

    def heal(self, amount):
        if self.__life == 0:
            return "Impossible de soigner un joueur mort."
        elif self.__life == 10:
            return "Les points de vie sont deja au maximum."
        elif self.__life + amount <= 10:
            self.__life += amount
            return f"Le joueur {self.player_name} a marque {amount} points de vie."
        else:
            self.__life = 10
            return f"Les points de vie de joueur {self.player_name} est maintenant au maximum (10 points)."

    def revive(self):
        if self.__life == 0:
            self.__life = 10
            return f"Le joueur {self.player_name} est revenu a la vie."
        else:
            return f"Le joueur {self.player_name} est deja en vie."

    def get_life(self):
        return f"Les points de vie actuellement est : {self.__life}"

class Compteur:
    def __init__(self):
        self.__count = 0

    def incremint(self):
        self.__count += 1

    def get_count(self):
        return self.__count

class Experience:
    def __init__(self):
        self.__xp = 0

    def add_xp(self, points):
        self.__xp += points 

    def get_xp(self):
        return self.__xp

class Game:
    def __init__(self, player_name):
        self.life = LifePoints(player_name)
        self.compteur = Compteur()
        self.xp = Experience()

    def attack(self, damage):
        self.compteur.incremint()
        message = self.life.take_damage(damage)
        self.xp.add_xp(10)
        return f"Attaque  numero {self.compteur.get_count()} : {message}"

joueur1 = LifePoints("Ammar")

print(joueur1.take_damage(3))
print(joueur1.take_damage(4))
print(joueur1.revive())
print(joueur1.take_damage(5))
print(joueur1.heal(5))
print(joueur1.take_damage(1))

print(joueur1.get_life())

print("-----")

joueur2 = LifePoints("Ali")

print(joueur2.take_damage(6))
print(joueur2.heal(3))
print(joueur2.heal(10))

print(joueur2.get_life())

print("-----")

joueur3 = LifePoints("Ahmed")

print(joueur3.take_damage(10))
print(joueur3.heal(3))
print(joueur3.revive())
print(joueur3.take_damage(4))
print(joueur3.heal(2))

print(joueur3.get_life())

print("-----")

game = Game("Ammar")
print(game.attack(3))
print(game.attack(4))
print(game.attack(8))
print("XP actuelle :", game.xp.get_xp())