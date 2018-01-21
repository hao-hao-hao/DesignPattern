from models import Charge_Behaviour

class Charge_at_Home(Charge_Behaviour):
    def charge(self):
        print("I am charging at home")
