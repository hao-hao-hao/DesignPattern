from models import Car
from models import Cant_Charge

class Sports_Car(Car):
    def __init__(self, registration):
        super().__init__(registration)
        self.charge_behaviour= Cant_Charge()
    def display(self):
        print("I am a Sports Car")
