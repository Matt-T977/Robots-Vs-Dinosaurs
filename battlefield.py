from herd import Herd
from fleet import Fleet


class Battlefield:    

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()


    def run_game(self):
        game_start = self.display_welcome()
        if game_start:
            play_again = "1"
            while play_again == "1":
                self.herd.create_herd()
                self.fleet.create_fleet()
                self.display_winners(self.battle())
                play_again = input("\nDo you wish to play again? 1: Yes 2: No \nPlayer: ")
        
    def display_welcome(self):
        game_start = input('''
        \nROBOTS VS DINOSAURS
        \nPress 1 to begin!
        \nPlayer:  ''')
        if game_start == "1":
            return True  
        else:
            return False

    def battle(self):
        game_continue = True
        while game_continue:
            game_continue = self.dino_turn(self.show_dino_options(), self.show_dino_opponent_options())
            if game_continue == False:
                return "Dinosaurs"
            game_continue = self.robo_turn(self.show_robo_options(), self.show_robo_opponent_options())
            if game_continue == False:
                return "Robots"

    def dino_turn(self, dinosaur, robot):
        self.herd.dinosaurs[dinosaur].attack(self.fleet.robots[robot])
        for robo in self.fleet.robots:
            if robo.alive == True:
                return True
        return False            

    def robo_turn(self, robot, dinosaur):
        self.fleet.robots[robot].attack(self.herd.dinosaurs[dinosaur])
        for dino in self.herd.dinosaurs:
            if dino.alive == True:
                return True
        return False

    def show_robo_options(self):
        invalid_choice = True
        while invalid_choice:
            player_choice = int(input(f'''
            \nPick your robot!
            \n1: {self.fleet.robots[0].name} HP: {self.fleet.robots[0].health}
            \n2: {self.fleet.robots[1].name} HP: {self.fleet.robots[1].health}
            \n3: {self.fleet.robots[2].name} HP: {self.fleet.robots[2].health}
            \nPlayer: ''')) - 1 
            if self.fleet.robots[player_choice].alive:
                return player_choice
            elif self.fleet.robots[player_choice].alive == False:
                print(f"{self.fleet.robots[player_choice].name} is already destroyed! Pick another Soldier Commander!")
            else:
                print("Invalid input try again.")

    def show_dino_options(self):
        invalid_choice = True
        while invalid_choice:
            player_choice = int(input(f'''
            \nPick your dinosaur!
            \n1: {self.herd.dinosaurs[0].name} HP: {self.herd.dinosaurs[0].health}
            \n2: {self.herd.dinosaurs[1].name} HP: {self.herd.dinosaurs[1].health}
            \n3: {self.herd.dinosaurs[2].name} HP: {self.herd.dinosaurs[2].health}
            \nPlayer: ''')) - 1
            if self.herd.dinosaurs[player_choice].alive:
                return player_choice
            elif self.herd.dinosaurs[player_choice].alive == False:
                print(f"{self.herd.dinosaurs[player_choice].name} is already dead! Pick another Dinosaur Alpha!")
            else:
                print("Invalid input try again.")

    def show_dino_opponent_options(self):
        invalid_target = True
        while invalid_target:
            player_target = int(input(f'''
            \nPick your dinosaur's attack target!
            \n1: {self.fleet.robots[0].name} HP: {self.fleet.robots[0].health}
            \n2: {self.fleet.robots[1].name} HP: {self.fleet.robots[1].health}
            \n3: {self.fleet.robots[2].name} HP: {self.fleet.robots[2].health}
            \nPlayer: ''')) - 1
            if self.fleet.robots[player_target].alive:
                return player_target
            elif self.fleet.robots[player_target].alive == False:
                print(f"{self.fleet.robots[player_target].name} is already destroyed! Pick another target Alpha!")
            else:
                print("Invalid input try again.")       

    def show_robo_opponent_options(self):
        invalid_target = True
        while invalid_target:
            player_target = int(input(f'''
            \nPick your robot's attack target!
            \n1: {self.herd.dinosaurs[0].name} HP: {self.herd.dinosaurs[0].health}
            \n2: {self.herd.dinosaurs[1].name} HP: {self.herd.dinosaurs[1].health}
            \n3: {self.herd.dinosaurs[2].name} HP: {self.herd.dinosaurs[2].health}
            \nPlayer: ''')) - 1
            if self.herd.dinosaurs[player_target].alive:
                return player_target
            elif self.herd.dinosaurs[player_target].alive == False:
                print(f"{self.herd.dinosaurs[player_target].name} is already dead! Pick another target Commander!")
            else:
                print("Invalid input try again.")    

    def display_winners(self, winners):
        if winners == "Dinosaurs":
            print("\nDinosaurs have trampled and dismantled the robot invasion. Skynet does not go online.")
        elif winners == "Robots":
            print("\nSkynet Online. Robots have managed to vaporize the dinosaurs making them extinct Commander... Again.")    