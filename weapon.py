class Weapon:
    def __init__(self):
        self.name = ""
        self.attack_power = 0

    def weapon_profile(self, profile):
        if profile == "Photon Cannon":
           self.name = "Photon Cannon"
           self.attack_power = 50
        elif profile == "Beam Rifle":
            self.name = "Beam Rifle"
            self.attack_power = 10
        elif profile == "Ion Lance":
            self.name = "Ion Lance"
            self.attack_power = 25       