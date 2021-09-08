from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []


    def create_herd(self):
        dinosaur_one = Dinosaur()
        dinosaur_two = Dinosaur()
        dinosaur_three = Dinosaur()
        self.dinosaurs = [dinosaur_one, dinosaur_two, dinosaur_three]
        self.herd_setup()

    def herd_setup(self):
        self.dinosaurs[0].dinosaur_setup(0)
        self.dinosaurs[1].dinosaur_setup(1)
        self.dinosaurs[2].dinosaur_setup(2)

    def herd_test(self):
        print(self.dinosaurs[0].name)
        print(self.dinosaurs[0].attack_power)
        print(self.dinosaurs[0].health)         