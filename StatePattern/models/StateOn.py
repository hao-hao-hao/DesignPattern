from models import State

class StateOn(State):
    
    @staticmethod
    def SwitchOn():
        print("You can't switch on again as it is already On")
    @staticmethod
    def SwitchOff():
        print("It is switched off")
        