from models import Car
from models import Charge_at_Home


class Eletric_Car(Car):
    def __init__(self,registration):
        super().__init__(registration)
        self.charge_behaviour = Charge_at_Home()

    def display(self):
        print("I am an eletric car")
