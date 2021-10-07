from robot import Robots
import random

from weapon import Weapon



class Fleet:
    def __init__(self):
        self.robots = []
        self.weapons = []
        
        
    
  

    def create_fleet(self):
        weapon1 = Weapon("Sword", 8)
        weapon2 = Weapon("AR-15", 13)
        weapon3 = Weapon("Knife", 11)
             
        Robo1 = Robots('MegaTron', 100, weapon1.attack_power)
        Robo2 = Robots('Skyscream', 100, weapon2.attack_power)
        Robo3 = Robots('BumbleBee', 100, weapon3.attack_power)
        self.robots.append(Robo1)
        self.robots.append(Robo2)
        self.robots.append(Robo3)
        

    def choose_robo(self):
        for items in self.robots:
            self.robot = random.choice(items)
    




# new = Fleet()
# new.create_fleet()
  