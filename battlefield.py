from herd import Herd
from fleet import Fleet


class Battlefield:    

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()


    def run_game(self):
        game_start = self.display_welcome()
        if game_start:
            play_again = "yes"
            while play_again == "yes":
                self.herd.create_herd()
                self.fleet.create_fleet()
                self.display_winners(self.battle())
                play_again = input("Do you wish to play again? Yes or No")
        
    def display_welcome(self):
        game_start = input('''
        \nROBOTS VS DINOSAURS
        \nType Start to begin!\n 
        ''').lower()
        if game_start == "start":
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
        print(self.fleet.robots[robot].health)
        for robo in self.fleet.robots:
            if robo.alive == True:
                return True
        return False            

    def robo_turn(self, robot, dinosaur):
        self.fleet.robots[robot].attack(self.herd.dinosaurs[dinosaur])
        print(self.herd.dinosaurs[dinosaur].health)
        for dino in self.herd.dinosaurs:
            if dino.alive == True:
                return True
        return False

    def show_robo_options(self):
        print(f'''
        \n1: {self.fleet.robots[0].name}
        \n2: {self.fleet.robots[1].name}
        \n3: {self.fleet.robots[2].name}\n''')
        player_choice = int(input("Pick your robot! ")) - 1
        return player_choice

    def show_dino_options(self):
        print(f'''
        \n1: {self.herd.dinosaurs[0].name}
        \n2: {self.herd.dinosaurs[1].name}
        \n3: {self.herd.dinosaurs[2].name}\n''')
        player_target = int(input("Pick your dinosaur! ")) - 1
        return player_target

    def show_dino_opponent_options(self):
        print(f'''
        \n1: {self.fleet.robots[0].name}
        \n2: {self.fleet.robots[1].name}
        \n3: {self.fleet.robots[2].name}\n''')
        player_target = int(input("Pick your dinosaur's attack target! ")) - 1
        return player_target

    def show_robo_opponent_options(self):
        print(f'''
        \n1: {self.herd.dinosaurs[0].name}
        \n2: {self.herd.dinosaurs[1].name}
        \n3: {self.herd.dinosaurs[2].name}\n''')
        player_target = int(input("Pick your robot's attack target! ")) - 1
        return player_target

    def display_winners(self, winners):
        if winners == "Dinosaurs":
            print("Dinosaurs have trampled and dismantled the robot invasion. Skynet does not go online.")
        elif winners == "Robots":
            print("Skynet Online. Robots have managed to vaporize the dinosaurs making them extinct... Again.")    
    '''
    -For each character object give them a true/false property indicating if still alive
    -At the end of each attack phase, do a check to see if their remaining HP > 0, if yes remain true / if no then false
    -Once turn concludes do a check to see if there are any remaining trues left on the enemy side.
    -If no, current turn side wins, If yes, game continues.
    '''