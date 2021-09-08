from weapon import Weapon


class Robot:
    def __init__(self):
        self.name = ""
        self.health = 75
        self.weapon_profile = ""
        self.weapon = Weapon()


    def attack(self, dinosaur):
        pass    