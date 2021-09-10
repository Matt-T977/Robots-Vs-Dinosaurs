class Dinosaur:
    def __init__(self):
        self.name = ""
        self.attack_power = 0
        self.attack_name = ("Bite", "Tail Whip", "Stomp", "Bash")
        self.health = 0
        self.alive = True

# Picks and loads in the chosen dino profile
    def dinosaur_setup(self, dinosaur_number):
        dinosaur_names = ["Raptor", "Trike", "Rex"]
        dinosaur_health = [50, 125, 100]
        dinosaur_attack = [15, 25, 75]
        self.name = dinosaur_names[dinosaur_number]
        self.health = dinosaur_health[dinosaur_number]
        self.attack_power = dinosaur_attack[dinosaur_number]

# Attack selector
    def attack_selection(self, robot):
        dino_attack = int(input(f'''
        \nWhat attack would you like to use?!
        \n1: {self.attack_name[0]}
        \n2: {self.attack_name[1]}
        \n3: {self.attack_name[2]}
        \n4: {self.attack_name[3]}
        \nPlayer: ''')) - 1
        print(f"\nThe {self.name} viciously attacks {robot.name} with a {self.attack_name[dino_attack]}!")

# Handles Damage Calculation and HP Display
    def attack(self, robot):
        self.attack_selection(robot)
        robot.health -= self.attack_power
        print(f"\n{robot.name} has {robot.health} HP remaining!")
        if robot.health <= 0:
            robot.alive = False