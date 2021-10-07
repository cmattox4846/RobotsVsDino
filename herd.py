from dinosaur import Dinosaurs
import random

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.selected_dinosaur = {}
        

    def create_herd(self):
        dino1 = Dinosaurs('TRex', 100, 12)
        dino2 = Dinosaurs('Stegosaurus', 100, 9)
        dino3 = Dinosaurs('Brontosaurus', 100, 11)
        self.dinosaurs.append(dino1)
        self.dinosaurs.append(dino2)
        self.dinosaurs.append(dino3)
        
        

    
            
    

