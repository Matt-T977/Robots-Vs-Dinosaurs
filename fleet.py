from robot import Robot


class Fleet:
    def __init__(self):
        self.robots = []


    def create_fleet(self):
        robot_one = Robot()
        robot_two = Robot()
        robot_three = Robot()
        self.robots = [robot_one, robot_two, robot_three]
        self.fleet_setup()  

    def fleet_setup(self):
        self.robots[0].name = "DSU-975-PC"
        self.robots[0].weapon_selection()
        self.robots[1].name = "DSU-976-BR"
        self.robots[1].weapon_selection()
        self.robots[2].name = "DSU-977-IL"
        self.robots[2].weapon_selection()