class Weapon:
    def __init__(self):
        self.name = ""
        self.attack_power = 0
        
# Takes load out selection and loads it into the weapon profile
    def weapon_profile(self, profile):
        if profile == "1":
           self.name = "Photon Cannon"
           self.attack_power = 50
        elif profile == "2":
            self.name = "Beam Rifle"
            self.attack_power = 10
        elif profile == "3":
            self.name = "Ion Lance"
            self.attack_power = 25       