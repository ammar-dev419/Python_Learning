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
    def __init__(self, name):
        self.name = name
        self.life = LifePoints(name)
        self.counter = Compteur()
        self.xp = Experience()

    def attack(self, damage):
        self.counter.incremint()
        message = self.life.take_damage(damage)
        self.xp.add_xp(10)
        return f"Attaque #{self.counter.get_count()}: {message}"
    
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
    
class Mage(Player):
    def attack(self, damage):
        return super().attack(damage * 2)
    
class Warrior(Player):
    def attack(self, damage):
        return super().attack(damage + 2)
        
class Archer(Player):
    def attack(self, damage):
        if damage < 4:
            return super().attack(damage)
        else:
            return super().attack(damage + 1)
        
class Trickplayer(Player):
    def attack(self, damage):
        message = super().attack(damage)
        self.xp.add_xp(10)
        return message
    
class Monster:
    def __init__(self, name, life):
        self.name = name
        self.life = life

    def take_damage(self, damage):
        self.life -= damage
        if self.life <= 0:
            self.life = 0
            return f"{self.name} defeated!"
        else:
            return f"{self.name} has {self.life} life remainnig."
        
    def attack(self, player):
        message = player.take_damage(5)
        return f"{self.name} attaks {player.name}: {message}"
        

player1 = Player("Ali")
mage = Mage("Omar")
warrior = Warrior("Sara")
archer = Archer("Lina")
trick = Trickplayer("Youssef")
monster = Monster("Dragon", 50)

print(player1.attack(3))
print(mage.attack(3))
print(warrior.attack(3))
print(archer.attack(4))
print(trick.attack(2),"\n")

print(monster.attack(player1))
print(monster.attack(mage))
print(monster.attack(warrior))
print(monster.attack(archer))
print(monster.attack(trick),"\n")

print(f"{player1.name} life: {player1.get_life()}")
print(f"{mage.name} life: {mage.get_life()}")
print(f"{warrior.name} life: {warrior.get_life()}")
print(f"{archer.name} life: {archer.get_life()}")
print(f"{trick.name} life: {trick.get_life()}\n")

print(f"{player1.name} XP: {player1.get_xp()}")
print(f"{mage.name} XP: {mage.get_xp()}")
print(f"{warrior.name} XP: {warrior.get_xp()}")
print(f"{archer.name} XP: {archer.get_xp()}")
print(f"{trick.name} XP: {trick.get_xp()}")