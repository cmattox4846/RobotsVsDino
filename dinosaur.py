
class Dinosaurs:
   
   
    def __init__(self, name, health, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = health
        pass
    
    
    def attack(self, robot):
        robot.health -= self.attack_power
        pass

    
    def __str__(self):
        return ("Type: " + self.name)
       
   

