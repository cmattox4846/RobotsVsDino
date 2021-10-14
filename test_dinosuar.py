import unittest
import dinosaur
from robot import Robots



class TestDinosuarAttack(unittest.TestCase):

    def setUp(self):
        self.robot = Robots("Roboman",100,30)
        self.dino = dinosaur.Dinosaurs('mike',100,25)

    def test_dino_attack(self):
        attack_health = dinosaur.Dinosaurs.attack(self.dino, self.robot)
        self.assertEqual(attack_health,75)



if __name__ == "__main__":
    unittest.main()

