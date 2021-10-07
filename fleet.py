from robot import Robots
import random

from weapon import Weapon



class Fleet:
    def __init__(self):
        self.robots = []
        self.robot = {}
        self.weapon.weapon_builder()
        
    def create_fleet(self):
        self.weapon.weapon_builder()
        W1 = self.weapon.weapons[0].attack_power
        W2 = self.weapon.weapons[1].attack_power
        W3 = self.weapon.weapons[2].attack_power
        Robo1 = Robots('MegaTron', 100, W1)
        Robo2 = Robots('Skyscream', 100, W2)
        Robo3 = Robots('BumbleBee', 100, W3)
        # Robo1 = Robots('MegaTron', 100, self.weapon[0].attack_power)
        # Robo2 = Robots('Skyscream', 100, self.weapon[1].attack_power)
        # Robo3 = Robots('BumbleBee', 100, self.weapon[2].attack_power)
        self.robots.append(Robo1)
        self.robots.append(Robo2)
        self.robots.append(Robo3)
        

    def choose_robo(self):
        for items in self.robots:
            self.robot = random.choice(items)
    





  