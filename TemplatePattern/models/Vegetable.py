from models import Meal
class Vegetable(Meal):  

    def Prepare(self):
        print(self._name+": preparing vegetables")
    
    def Cook(self):
        print(self._name +": stir frying vegetables")
        