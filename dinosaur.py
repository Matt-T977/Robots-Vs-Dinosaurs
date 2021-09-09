


class Dinosaur:
    def __init__(self):
        self.name = ""
        self.attack_power = 0
        self.health = 0
        self.alive = True


    def dinosaur_setup(self, dinosaur_number):
        dinosaur_names = ["Raptor", "Trike", "Rex"]
        dinosaur_health = [50, 125, 100]
        dinosaur_attack = [10, 25, 75]
        self.name = dinosaur_names[dinosaur_number]
        self.health = dinosaur_health[dinosaur_number]
        self.attack_power = dinosaur_attack[dinosaur_number]

    def attack(self, robot):
        robot.health -= self.attack_power
        if robot.health <= 0:
            robot.alive = False