from dinosaur import Dinosaurs
import random

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.selected_dinosaur = {}
        

    def create_herd(self):
        dino1 = Dinosaurs('TRex', 100, 55)
        dino2 = Dinosaurs('Stegosaurus', 100, 23)
        dino3 = Dinosaurs('Brontosaurus', 100, 28)
        self.dinosaurs.append(dino1)
        self.dinosaurs.append(dino2)
        self.dinosaurs.append(dino3)
        # for item in self.dinosaurs:
        #     print(item)
        

    
            
    
# new = Herd()
# new.create_herd() 
        
