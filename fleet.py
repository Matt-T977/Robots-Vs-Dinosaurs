from robot import Robot


class Fleet:
    def __init__(self):
        self.robots = list


    def create_fleet(self):
        robot_one = Robot()
        robot_two = Robot()
        robot_three = Robot()
        self.robots = [robot_one, robot_two, robot_three]
        self.fleet_setup()  

    def fleet_setup(self):
        self.robots[0].weapon_profile = "Photon Cannon"
        self.robots[0].weapon.weapon_profile(self.robots[0].weapon_profile)
        self.robots[1].weapon_profile = "Beam Rifle"
        self.robots[1].weapon.weapon_profile(self.robots[1].weapon_profile)
        self.robots[2].weapon_profile = "Ion Lance"
        self.robots[2].weapon.weapon_profile(self.robots[2].weapon_profile)