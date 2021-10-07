from math import fabs
import random
import sys
from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.herd.create_herd()
        self.fleet.create_fleet()
        

    def run_game(self):
        self.display_welcome()
        
    
    def display_welcome(self):
        print("Welcome the to battle!")
        choice = input("Please choose who to fight as! \n 1 for Dinosaurs \n 2 for Robots \n")
        # answer = False
        # while answer == False:
        if choice == "1":
            self.show_dino_opponet_options()

        else:
            self.show_robo_opponenet_options()

       

    def battle(self, choice, opponent):
        dino_health = 100
        robot_health = 100
        battle_over =False
        while battle_over == False:
            number = random.choice([1,2])
            print(number)
            if number == 1:
                dino_health = self.dino_turn(choice, opponent)
                robot_health = self.robot_turn(opponent,choice)
            elif number == 2:
                robot_health = self.robot_turn(opponent,choice)
                dino_health = self.dino_turn(choice, opponent)
            if dino_health <= 0:
                battle_over = True
            elif robot_health <= 0:
                battle_over = True 
                

        
        if dino_health >= 0:
            winner = "Dinosaurs!"
            self.display_winner(winner)
        elif robot_health >= 0:
            winner = "Robots!"
            self.display_winner(winner)
            
        
       

    def dino_turn(self, dinosaur, robot_to_attack):
        robo_health = dinosaur.attack(robot_to_attack)
        print(f"Robots health is now: {robot_to_attack.health}")
        return robo_health
        

    def robot_turn(self, robot, dino_to_attack):
        dino_health = robot.attack(dino_to_attack)
        print(f'Dinos health is now: {dino_to_attack.health}')
        return dino_health
       

    def show_dino_opponet_options(self):
        answer = "0"
        while answer == "0":
            dino = random.choice(self.herd.dinosaurs)
            answer = input(f'You dino fighter will be {dino.name}\n Ready to fight type 1!\n To choose another dino type 2\n')
            if answer == '1':
                robot_fighter = random.choice(self.fleet.robots)
                self.battle(dino, robot_fighter)
            elif answer == "2":
                answer = "0"
            else:
                print("Please only choose 1 or 2")
                answer = "0"

        

    def show_robo_opponenet_options(self):
        answer = "0"
        while answer == "0":
            robo = random.choice(self.fleet.robots)
            answer = input(f'You dino fighter will be {robo.name}\n Ready to fight type 1!\n To choose another robot type 2\n')
            if answer == '1':
                dino_fighter = random.choice(self.herd.dinosaurs)
                self.battle(robo, dino_fighter)
            elif answer == "2":
                answer = "0"
            else:
                print("Please only choose 1 or 2")
                answer = "0"
       

    def display_winner(self, winner):
        print(f'The winner is {winner}! Thanks for playing')
        answer = input('Would you like to play again?\n 1- Play Again\n 2- End Game\n Enter Choice: ')
        if answer == "1":
             self.display_welcome()
        else:
            sys.exit()

        

# battle = Battlefield()
# battle.show_dino_opponet_options()