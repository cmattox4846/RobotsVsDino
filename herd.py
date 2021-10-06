import random
from dinosaur import Dinosaurs
import random

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.dinosaur = {}
        pass

    def create_heard(self):
        dino1 = Dinosaurs('TRex', 100, 55)
        dino2 = Dinosaurs('Stegosaurus', 100, 23)
        dino3 = Dinosaurs('Brontosaurus', 100, 28)
        self.dinosaurs.append[{dino1}]
        self.dinosaurs.append[{dino2}]
        self.dinosaurs.append[{dino3}]
        pass

    def choose_dino(self):
        for items in self.dinosaurs:
            self.dinosaur = random.choice(items)
    
    def __str__(self):
        return self.dinosaur
        pass
