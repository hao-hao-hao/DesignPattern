from models import Meal
class Meat(Meal):  

    def Prepare(self):
        print(self._name+": preparing Meat")
    
    def Cook(self):
        print(self._name +": grilling meat")
    
    def Hook(self):
        print(self._name+": serving with wine")
        