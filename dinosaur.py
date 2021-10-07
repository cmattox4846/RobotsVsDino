
class Dinosaurs:
   
   
    def __init__(self, name, health, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = health
        
    
    
    def attack(self, robot):
        robot.health -= self.attack_power
        return robot.health
       

    
    def __str__(self):
        return ("Type: " + self.name)
       
   

