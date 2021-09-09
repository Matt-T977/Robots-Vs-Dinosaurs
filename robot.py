from dinosaur import Dinosaur
from weapon import Weapon


class Robot:
    def __init__(self):
        self.name = ""
        self.weapon_profile = ""
        self.weapon = Weapon()
        self.health = 75
        self.alive = True


    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        if dinosaur.health <= 0:
            dinosaur.alive = False