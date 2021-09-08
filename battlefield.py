from herd import Herd
from fleet import Fleet
from dinosaur import Dinosaur
from robot import Robot


class Battlefield:    

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()


    def run_game(self):
        self.display_welcome(self)
        self.herd.create_herd()
        self.herd.herd_setup()
        self.fleet.create_fleet()
        self.fleet.fleet_setup()
        
    def display_welcome(self):
        game_start = input('''ROBOTS VS DINOSAURS\n
        Type Start to begin!\n 
        ''')

    def battle(self):
        pass

    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass