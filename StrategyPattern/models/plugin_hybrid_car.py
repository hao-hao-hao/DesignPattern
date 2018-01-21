from models import Car
from models import Charge_at_Station


class Plugin_Hybrid_Car(Car):
    def __init__(self, registration):
        super().__init__(registration)
        self.charge_behaviour = Charge_at_Station()
    def display(self):
        print("I am a PHEV Car")
