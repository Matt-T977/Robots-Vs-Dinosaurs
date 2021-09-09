from weapon import Weapon


class Robot:
    def __init__(self):
        self.name = ""
        self.weapon = Weapon()
        self.health = 75
        self.alive = True

    def weapon_selection(self):
        weapon_profile = input(f"""
        \nWhich weapon would you like to equip for {self.name}? 
        \n1: Photon Cannon: Attack Power - 50 
        \n2: Beam Rifle: Attack Power - 10
        \n3: Ion Lance: Attack Power - 25
        \nPlayer: """)
        self.weapon.weapon_profile(weapon_profile)

    def attack(self, dinosaur):
        print(f"\n{self.name} blasts the {dinosaur.name} with their {self.weapon.name}!")
        dinosaur.health -= self.weapon.attack_power
        print(f"\n{dinosaur.name} has {dinosaur.health} remaining!")
        if dinosaur.health <= 0:
            dinosaur.alive = False