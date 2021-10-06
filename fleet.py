from robot import Robots
import random



class Fleet:
    def __init__(self):
        self.robots = []
        self.robot = {}
        
    def create_fleet(self):
        Robo1 = Robots('MegaTron', 100)
        Robo2 = Robots('Skyscream', 100)
        Robo3 = Robots('BumbleBee', 100)
        self.robots.append[Robo1]
        self.robots.append[Robo2]
        self.robots.append[Robo3]
        print(self.robots)

    def choose_robo(self):
        for items in self.robots:
            self.robot = random.choice(items)
    





  