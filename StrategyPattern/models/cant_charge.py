from models import Charge_Behaviour

class Cant_Charge(Charge_Behaviour):
    def charge(self):
        print("I can't charge my car")
