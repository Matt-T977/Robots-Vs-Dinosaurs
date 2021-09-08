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
            self.fleet.fleet_setup()
        
    def display_welcome(self):
        game_start = input('''ROBOTS VS DINOSAURS\n
        Type Start to begin!\n 
        ''').lower()
        if game_start == "start":
            return True  
        else:
            return False

    def battle(self):
        self.dino_turn(self.show_dino_opponent_options())
        self.robo_turn(self.show_robo_opponent_options())

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