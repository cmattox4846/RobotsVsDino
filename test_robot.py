import unittest
import dinosaur
from robot import Robots



class TestRobotAttack(unittest.TestCase):

    def setUp(self):
        self.robot = Robots("Roboman",100,30)
        self.dino = dinosaur.Dinosaurs('mike',100,25)

    def test_dino_attack(self):
        attack_health = Robots.attack(self.robot, self.dino)
        self.assertEqual(attack_health,70)



if __name__ == "__main__":
    unittest.main()
