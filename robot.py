from weapon import Weapon
import random

class Robots:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.weapons = []
        
        
        pass

    def attack(self, dinosaur):
        dinosaur.health -= self.attack_power
        return dinosaur.health
        

    def weapon_builder(self):    
        weapon1 = Weapon("Sword", 33)
        weapon2 = Weapon("AR-15", 24)
        weapon3 = Weapon("Knife", 15)
        self.weapons.append(weapon1)
        self.weapons.append(weapon2)
        self.weapons.append(weapon3)
        for item in self.weapons:
            print(item)
        
        pass

    def select_weapon(self):
        for items in self.weapons:
            self.weapon = random.choice(items)
            

    def __str__(self):
        return ("Weapon is: " + self.weapon)


