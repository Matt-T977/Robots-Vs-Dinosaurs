from herd import Herd
from fleet import Fleet
from dinosaur import Dinosaur
from robot import Robot


class Battlefield:    

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()


    def run_game(self):
        game_start = self.display_welcome()
        if game_start:
            self.herd.create_herd()
            self.fleet.create_fleet()
            self.battle()
        
    def display_welcome(self):
        game_start = input('''ROBOTS VS DINOSAURS\n
        Type Start to begin!\n 
        ''').lower()
        if game_start == "start":
            return True  
        else:
            return False

    def battle(self):
        self.dino_turn(self.show_dino_options(), self.show_dino_opponent_options())
        self.robo_turn(self.show_robo_options(), self.show_robo_opponent_options())

    def dino_turn(self, dinosaur, robot):
        self.herd.dinosaurs[dinosaur].attack(self.fleet.robots[robot].health)
        print(self.fleet.robots[robot].health)

    def robo_turn(self, robot, dinosaur):
        self.fleet.robots[robot].attack(self.herd.dinosaurs[dinosaur].health)
        print(self.herd.dinosaurs[dinosaur].health)

    def show_robo_options(self):
        print(f'1:{self.fleet.robots[0].name}\n2:{self.fleet.robots[1].name}\n3:{self.fleet.robots[2].name}')
        player_choice = int(input("Pick your robot!")) - 1
        return player_choice

    def show_dino_options(self):
        print(f'1:{self.herd.dinosaurs[0].name}\n2:{self.herd.dinosaurs[1].name}\n3:{self.herd.dinosaurs[2].name}')
        player_target = int(input("Pick your dinosaur!")) - 1
        return player_target

    def show_dino_opponent_options(self):
        print(f'1:{self.fleet.robots[0].name}\n2:{self.fleet.robots[1].name}\n3:{self.fleet.robots[2].name}')
        player_target = int(input("Pick your dinosaur's attack target!")) - 1
        return player_target

    def show_robo_opponent_options(self):
        print(f'1:{self.herd.dinosaurs[0].name}\n2:{self.herd.dinosaurs[1].name}\n3:{self.herd.dinosaurs[2].name}')
        player_target = int(input("Pick your robot's attack target!")) - 1
        return player_target

    def display_winners(self):
        pass