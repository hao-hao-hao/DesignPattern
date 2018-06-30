from models import State

class StateOff(State):
    @staticmethod
    def SwitchOn():
        print("It is switched on")
    @staticmethod
    def SwitchOff():
        print("You can't switch off as it is already off")
        