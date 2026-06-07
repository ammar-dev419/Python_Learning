import random
class Character:
    def __init__(self, name, life):
        self.name = name
        self.life = life

    def take_damage(self, damage):
        if self.life == 0:
            return f"{self.name} est deja mort."
        elif self.life - damage > 0:
            return f"{self.name} est perdu {damage} points de vie."
        else:
            self.life = 0
            return f"{self.name} est mort."
        
    def is_alive(self):
        return self.life > 0
        
    def attack(self, target):
        pass


class Player(Character):
    def __init__(self, name, life):
        super().__init__(name, life)
        self.xp = 0
    
    def attack(self, target):
        damage = random.randint(3, 10)
        message = target.take_damage(damage)
        self.xp += 10
        return f"{self.name} attacks {target.name}\n{message}\nXP: {self.xp}"
    

class Mage(Player):
    def attack(self, target):
        damage = random.randint(3, 10) * 2
        message = target.take_damage(damage)
        self.xp += 10
        return f"{self.name} casts spell on {target.name}\n{message}\nXP: {self.xp}"
    

class Warrior(Player):
    def attack(self, target):
        damage = random.randint(3, 10) + 2
        message = target.take_damage(damage)
        self.xp += 10
        return f"{self.name} strikes {target.name}\n{message}\nXP: {self.xp}"
    

class Monster(Character):
    def attack(self, target):
        damage = 5
        message = target.take_damage(damage)
        return f"{self.name} attacks {target.name}\n{message}"


def battle(a, b):
    print(a.attack(b))
    if b.is_alive():
        print(b.attack(a))
    else:
        print(f"{b.name} is dead and cannot attack.")

if __name__ == "__main__":
    player1 = Player("Ali", 100)
    mage1 = Mage("Merlin", 80)
    warrior1 = Warrior("Thor", 120)
    monster1 = Monster("Dragon", 150)

    print("=== Player vs Monster ===")
    battle(player1, monster1)

    print("\n=== Mage vs Monster ===")
    battle(mage1, monster1)

    print("\n=== Warrior vs Player===")
    battle(warrior1, player1)

    print("\n=== Mage vs warrior===")
    battle(mage1, warrior1)

    print("\n=== Final States ===")

    print(f"{player1.name} alive: {player1.is_alive()}")
    print(f"{mage1.name} alive: {mage1.is_alive()}")
    print(f"{warrior1.name} alive: {warrior1.is_alive()}")
    print(f"{monster1.name} alive: {monster1.is_alive()}")