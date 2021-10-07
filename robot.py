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
        


  
    def __str__(self):
        return ("Weapon is: " + self.weapon)


