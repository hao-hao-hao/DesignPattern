from models import Charge_Behaviour 
from models import Cant_Charge


class Car():
    """Base class of all cars"""

    def __init__(self, registration):
        self._registration = registration
        self._charge_behaviour = Cant_Charge()

    @property
    def registration(self):
        return self._registration

    @property
    def charge_behaviour(self):
        return self._charge_behaviour

    @charge_behaviour.setter
    def charge_behaviour(self, value):
        """only allow to set behaviour if it is the instance of Charge_Behaviour
        """
        if(isinstance(value,Charge_Behaviour)):
            self._charge_behaviour = value
        else:
            print("Sorry, the behaviour you selected is not a charge behaviour")

 
    def display(self):
        print("I am a basic car")

    def start_engine(self):
        print("engine is started")

    def headlights_on(self):
        print("headlights are on")

   
    def charge(self):
        self.charge_behaviour.charge()

