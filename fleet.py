from robot import Robot


class Fleet:
    def __init__(self):
        self.robots = []

# Creates the robot characters and starts the set up.
    def create_fleet(self):
        robot_one = Robot()
        robot_two = Robot()
        robot_three = Robot()
        self.robots = [robot_one, robot_two, robot_three]
        self.fleet_setup()  

# Sets robot names and start the load out custimization for players.
    def fleet_setup(self):
        print('''
        \nThe fleet has arrived Commander! 
        \nPlease select our squad's armament Commander!''')
        self.robots[0].name = "DSU-975-PC"
        self.robots[0].weapon_selection()
        self.robots[1].name = "DSU-976-BR"
        self.robots[1].weapon_selection()
        self.robots[2].name = "DSU-977-IL"
        self.robots[2].weapon_selection()