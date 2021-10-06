from random import choice
from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.fleet = Fleet
        self.herd = Herd
        pass

    def run_game(self):
        self.display_welcome()
        pass
    
    def display_welcome(self):
        print("Welcome the to battle!")
        choice = input("Please choose who to fight as! \n 1 for Dinosaurs \n 2 for Robots \n")
        answer = False
        while answer == False:
            if choice == "1":
               answer = self.show_dino_opponet_options()

            else:
               answer = self.show_robo_opponenet_options()

        pass

    def battle(self, choice):
        dino_health = 100
        robot_health = 100
        while dino_health != 0 or robot_health != 0:
            self.dino_turn(choice)
            self.robot_turn(choice)
        pass

    def dino_turn(self, dinosaur):
        self.herd
        pass

    def robot_turn(self, robot):
        pass

    def show_dino_opponet_options(self):
        dino = self.herd.choose_dino
        answer = input(f'You dino fighter wwill be {self.herd.choose_dino}\n Ready to fight type 1!\n To choose another dino type 2\n')
        if answer == '1':
            self.battle(dino)
        else:
            return False

        pass

    def show_robo_opponenet_options(self):
        answer = input(f'You dino fighter wwill be {self.fleet.choose_dino}\n Ready to fight type 1!\n To choose another robot type 2\n')
        if answer == '1':
           self.battle()
        else:
            return False
        pass

    def display_winner(self):
        print(f'The winner is! Thanks for playing')
        pass