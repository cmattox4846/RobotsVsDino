import unittest
from fleet import Fleet
from weapon import Weapon




class TestFleetCreation(unittest.TestCase):

    def setUp(self):
        self.new_fleet = Fleet()
        
        

    def test_herd_create(self):
        self.new_fleet.create_fleet()
        self.assertEqual(len(self.new_fleet.robots),3)
              



if __name__ == "__main__":
    unittest.main()