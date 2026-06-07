class LifePoints:
    def __init__(self, player_name):
        self.player_name = player_name
        self.__life = 10

    def take_damage(self, damage):
        if self.__life == 0:
            return f"{self.player_name} est deja mort."
        elif self.__life - damage > 0:
            self.__life -= damage
            return f"Le joueur {self.player_name} a perdu {damage} points du vie."
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

class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.life = LifePoints(player_name)
        self.counter = Compteur()
        self.xp = Experience()

    def attack(self, damage):
        self.counter.incremint()
        message = self.life.take_damage(damage)
        self.xp.add_xp(10)
        return f"{self.player_name} attaque #{self.counter.get_count()} : {message}"
    
    def take_damage(self, damage):
        return self.life.take_damage(damage)

    def heal(self, amount):
        return self.life.heal(amount)
    
    def revive(self):
        return self.life.revive()
    
    def get_life(self):
        return self.life.get_life()
    
    def incremint(self):
        return self.counter.incremint()
    
    def get_count(self):
        return self.counter.get_count()

    def add_xp(self, points):
        return self.xp.add_xp(points)

    def get_xp(self):
        return self.xp.get_xp()
        

player1 = Player("Ali")

print(player1.get_life())

print(player1.attack(3))

print(player1.get_count())

print(player1.get_xp())

print(player1.heal(5))

print(player1.attack(15))

print(player1.revive())