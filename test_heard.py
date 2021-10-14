import unittest
from herd import Herd




class TestHeardCreation(unittest.TestCase):

    def setUp(self):
        self.new_herd = Herd()
        

    def test_herd_create(self):
        self.new_herd.create_herd()
        self.assertEqual(len(self.new_herd.dinosaurs),3)



if __name__ == "__main__":
    unittest.main()
